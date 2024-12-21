# csvenvelopes

Scripts I use to make envelopes for Christmas cards.

Note: currently this is set up to use tab-separated values instead of comma-separated ones.

Usage:

```
$ tail -n +2 addresses.tsv  | ./make_lines.py  | ./make_envelopes.py  > out.pdf
```
