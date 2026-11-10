# Live client code-review demo

نسخة تجريبية وهمية لعرض Code Intelligence أمام العميل.

1. Start with the known-good baseline on `main`:12 tests pass.
2. During the presentation, publish the prepared intentionally incorrect version.
3. Click **Check now** in Code Intelligence to retrieve the new GitHub commit.

The prepared change removes an authorization check and breaks percentage-discount arithmetic. It affects only synthetic in-memory dictionaries and decimal calculations. No real accounts, network operations, credentials or private data are involved.

```bash
python -m unittest discover -s tests -v
```

Expected after publishing the intentionally incorrect version:6 tests fail,6 pass. A code-review report should flag critical authorization risk and propose security and pricing regression cases. Suggested tests are separate from measured unittest results.
