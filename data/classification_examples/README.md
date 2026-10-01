# Worked example of a classification reply

`EXAMPLE-IC-0014.json` shows the reply format `pipeline/classify.py --apply` accepts, for record IC-0014
(*Consequences* by Aaron Fraire). The assistant wrote it on 2026-09-30 by reading the record's performance
text. It is an example and has not been applied to the database. Every quoted phrase in its evidence occurs in
the performance text. Content-warning evidence must quote the performance text; a quote from the introduction or
the source block is rejected.

Check it without writing anything:

    python pipeline/classify.py --apply data/classification_examples/EXAMPLE-IC-0014.json --dry-run

Note: this record's performance text currently also contains a casting note, a character description and a
suggested introduction (a gap in the `publisher_script` parser, reported in Phase 5). The example deliberately
quotes only spoken lines.
