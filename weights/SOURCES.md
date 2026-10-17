# Checkpoint provenance

Original app repository: [bharathlogs/Coffee-Leaf-Disease-Detection](https://github.com/bharathlogs/Coffee-Leaf-Disease-Detection), reviewed at commit `9bf392da97ff26c08f8770614f463d56cc892ace`.

Restored checkpoints: [FTsune/kape](https://github.com/FTsune/kape/tree/f6b806e093659e0ce44cc47d993d05b1832de424/weights), pinned commit `f6b806e093659e0ce44cc47d993d05b1832de424`.
Downloaded blobs were checked against the source repository's Git blob SHA-1 identifiers before use. Files were not retrained or converted.

| File | SHA-256 |
| --- | --- |
| `cleaf.pt` | `7072da902ef8dbd77d79b03bc12961e0d8a0582b39eef9dbc226712e1b24a563` |
| `spots.pt` | `e05d2c6023cc2fa7bded23d4394f91b25dbfcb8ee729d92ab71d1a388bb9f938` |
| `yolo12n.pt` | `388ef7eb15a61fd275a8902b74853d08188415bb26250e34080541603c4e2a88` |

`cdisease.pt` and `yolo11m96.pt` were already present in the original repository. The donor's other four unused checkpoints are not included; these five files cover every model used by the application's Disease, Leaf and Both Models modes.

Keep the original checkpoint metadata and attribution. The donor repository does not declare a repository-level license; confirm model/data reuse permissions before broader redistribution. Ultralytics dependency terms are separate from the application repository's MIT license.
