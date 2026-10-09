#!/usr/bin/env perl
# Check a classification reply against its batch file before it is applied (no Python needed).
#   perl tools/check_reply.pl data/classification_requests/batch-001.md data/classification_replies/batch-001-reply.json
# The same rules as pipeline/classify.py --apply (allowed values, confidence, evidence, content warnings quoting the
# performance text, audience level only with content warnings, protected fields), plus two stricter checks:
#   * every quoted phrase in any evidence must occur in that record's text (performance text, introduction or source)
#   * every record in the batch has a reply with at least the four key fields
# Prints one line per problem and "OK: ..." when there are none; exit status 1 if any problem.
use strict;
use warnings;
use utf8;
use JSON::PP;
binmode STDOUT, ":encoding(UTF-8)";

my ($batch, $reply) = @ARGV;
die "usage: perl tools/check_reply.pl BATCH.md REPLY.json\n" unless $batch && $reply;
my $root = $0; $root =~ s{tools/check_reply\.pl$}{}; $root = "" unless $0 =~ m{tools/check_reply.pl$};

sub slurp { my ($p) = @_; open my $f, "<:encoding(UTF-8)", $p or die "cannot read $p: $!\n"; local $/; my $s = <$f>; close $f; $s }
sub norm {
    my ($s) = @_;
    $s =~ tr/\x{2019}\x{2018}\x{201C}\x{201D}/''""/;
    $s =~ s/\x{2026}/.../g;
    $s =~ s/\s+/ /g; $s =~ s/^ | $//g;
    return lc $s;
}
sub quotes { my $n = norm($_[0]); my @q; while ($n =~ /"([^"]{3,300})"/g) { my $x = $1; my @w = split ' ', $x; push @q, $x if @w >= 2 } @q }

my $tax = JSON::PP->new->utf8->decode(do { open my $f, "<:raw", "${root}data/taxonomy.json" or die "taxonomy: $!\n"; local $/; <$f> });
my %vocab = map { $_ => [ grep { $_ ne "Not specified" && $_ ne "Not assessed" } keys %{ $tax->{fields}{$_}{values} } ] }
            qw(literary_form tone content_warnings difficulty performance_demands audience_level);
my %kind = (literary_form => "enum", difficulty => "enum", audience_level => "enum", tone => "multi",
            content_warnings => "multi", performance_demands => "multi", themes => "list", subject_matter => "text");
my @KEY = qw(tone content_warnings difficulty literary_form);

# --- the batch: records with their texts and protected fields
my $md = slurp($batch);
my (%rec, @order);
for my $blk (split /^---\n/m, $md) {
    next unless $blk =~ /^## (IC-\d+): /m;
    my $id = $1; push @order, $id;
    my %r;
    ($r{perf})  = $blk =~ /### Performance text \(classify this\)\n\n```text\n(.*?)\n```\n/s;
    ($r{intro}) = $blk =~ /### Introduction \(context only[^\n]*\n\n```text\n(.*?)\n```\n/s;
    ($r{src})   = $blk =~ /### Source block \(context only\)\n\n```text\n(.*?)\n```\n/s;
    my ($kept)  = $blk =~ /^- Already set \(do not supply\): (.*)$/m;
    $r{protected} = { map { (split / = /)[0] => 1 } grep { $_ ne "none" } split /; /, ($kept // "none") };
    $r{$_} = norm($r{$_} // "") for qw(perf intro src);
    $rec{$id} = \%r;
}
die "no records found in $batch\n" unless @order;

# --- the reply
my $data = eval { JSON::PP->new->utf8->relaxed(0)->decode(do { open my $f, "<:raw", $reply or die "cannot read $reply: $!\n"; local $/; <$f> }) };
if (!$data || ref $data ne "HASH") { print "PROBLEM reply: not one valid JSON object (", ($@ =~ s/\s+$//r), ")\n"; exit 1 }

my @p;
for my $id (@order) { push @p, "$id: no reply for this record" unless $data->{$id} }
for my $id (sort keys %$data) {
    my $r = $rec{$id};
    if (!$r) { push @p, "$id: not a record in this batch"; next }
    my $f = $data->{$id};
    if (ref $f ne "HASH") { push @p, "$id: expected an object of fields"; next }
    for my $k (@KEY) { push @p, "$id: key field $k missing" unless $f->{$k} || $r->{protected}{$k} }
    for my $name (sort keys %$f) {
        my ($it, $w) = ($f->{$name}, "$id.$name");
        if (!$kind{$name}) { push @p, "$w: not a field the AI may supply"; next }
        if ($r->{protected}{$name}) { push @p, "$w: already set by the source or a reviewer; leave it out"; next }
        if (ref $it ne "HASH" || !exists $it->{value}) { push @p, "$w: expected {value, confidence, evidence}"; next }
        my ($v, $c, $ev) = @$it{qw(value confidence evidence)};
        push @p, "$w: confidence must be high, medium or low" unless defined $c && $c =~ /^(high|medium|low)$/;
        if (!defined $ev || ref $ev || $ev !~ /\S/) { push @p, "$w: evidence is required"; next }
        push @p, "$w: evidence longer than 400 characters" if length $ev > 400;
        my $kd = $kind{$name};
        if ($kd eq "enum") {
            push @p, "$w: '" . ($v // "") . "' is not an allowed value" unless defined $v && !ref $v && grep { $_ eq $v } @{ $vocab{$name} };
        } elsif ($kd eq "multi") {
            if (ref $v ne "ARRAY") { push @p, "$w: expected a list" }
            else { my @bad = grep { my $x = $_; !grep { $_ eq $x } @{ $vocab{$name} } } @$v; push @p, "$w: not allowed values: @bad" if @bad }
        } elsif ($kd eq "list") {
            if (ref $v ne "ARRAY" || grep { ref $_ || $_ !~ /\S/ } @$v) { push @p, "$w: expected a list of short phrases" }
            elsif (@$v > 8 || grep { length($_) >= 60 } @$v) { push @p, "$w: at most 8 themes of under 60 characters each" }
        } else {
            push @p, "$w: expected one sentence" unless defined $v && !ref $v && $v =~ /\S/;
            push @p, "$w: longer than 300 characters" if defined $v && !ref $v && length $v > 300;
        }
        my @q = quotes($ev);
        for my $q (@q) {
            next if index($r->{perf}, $q) >= 0 || index($r->{intro}, $q) >= 0 || index($r->{src}, $q) >= 0;
            push @p, "$w: quoted \"$q\" is not in this record's text";
        }
        if ($name eq "content_warnings") {
            my @out = grep { index($r->{perf}, $_) < 0 && (index($r->{intro}, $_) >= 0 || index($r->{src}, $_) >= 0) } @q;
            push @p, "$w: evidence quotes the introduction or source block, not the performance text" if @out;
            push @p, "$w: evidence must quote the performance text in double quotes"
                if ref $v eq "ARRAY" && @$v && !grep { index($r->{perf}, $_) >= 0 } @q;
        }
        if ($name eq "audience_level" && !$f->{content_warnings}) { push @p, "$w: needs content_warnings in the same reply" }
    }
}
if (@p) { print "PROBLEM $_\n" for @p; print scalar(@p), " problem(s) in $reply\n"; exit 1 }
printf "OK: %d records, %d values, every quote found in its record's text\n", scalar(keys %$data), scalar(map { keys %$_ } values %$data);
exit 0;
