# Trace Map — EQ-0001 + EQ-0002

Mode: non-synthesis trace map from extraction outputs only.

## Control State

| Control | State |
|---|---|
| synthesis_across_SDG_SEC_RTFA | not_performed |
| canon_promotion | not_performed |
| files3_member_extraction | not_performed |
| 4_5_5_content_synthesis | not_performed |

## Input Evidence Artifacts

| EQ | Evidence artifact | Source | Source SHA256 | Status |
|---|---|---|---|---|
| EQ-0001 | EQ-0001_4_5_5_segmentation_pass.json | 4.5.5.txt | `afdb379a795364c867db3e27411d447a721990a81e474c5620bd575925dd56cf` | SEGMENTED_NOT_SYNTHESIZED |
| EQ-0002 | EQ-0002_files3_zip_inventory.json | files3.zip | `fab9953dd947504ba9c4bf952a2c9292a072786bfbeee2237729e546fbaea2d4` | INVENTORIED_NOT_EXTRACTED |

## EQ-0001 Marker Counts

| Marker | Count |
|---|---:|
| BEGIN_PREVIOUS_SESSION | 1 |
| END_PREVIOUS_DAX | 0 |
| USER_SAID | 17 |
| CHATGPT_SAID | 0 |
| ASSISTANT_THOUGHT_MODEL | 14 |
| PROMPT_LABEL | 1 |
| SOURCES_LABEL | 72 |
| FAILED_FILE_READ | 0 |

## EQ-0001 Flag Counts

| Flag | Segment count |
|---|---:|
| contains_file_attachment_word | 23 |
| contains_stop | 28 |
| contains_suno | 83 |

## EQ-0001 Phrase Hit Counts

| Phrase | Hit count |
|---|---:|
| `Suno v4.5` | 281 |
| `Council Decision Matrix` | 31 |
| `virtual SME` | 23 |
| `world-class` | 23 |
| `Scalable Songwriting` | 20 |
| `[ key | variable.x ]` | 10 |
| `PoC Mode` | 7 |
| `Conversation Pass Pipeline` | 5 |
| `5 areas` | 3 |
| `sense-think-research-question-act` | 2 |
| `web based gpt and suno` | 1 |

## EQ-0002 Member Inventory

| Member | Kind | Lines | Bytes | SHA256 | Status |
|---|---|---:|---:|---|---|
| `maestro_v5c_bootstrap.md` | text/md | 484 | 26055 | `58bba55491c10c19440aa96b6ec42083f0779b531f2d536be37ccf631fdb2343` | INVENTORIED_NOT_EXTRACTED |
| `MOSAIC_system_architecture.svg` | text/svg | 276 | 14620 | `d47e6e48d7730458e4ba20984962a53c0ac246d9048d3becb7065949f6131a6c` | INVENTORIED_NOT_EXTRACTED |
| `BASELINE_RECONSTRUCTION_LEDGER_v0.1.docx` | docx |  | 18952 | `8c5ca9a594b22a5bcfcfde36d56fce23c79b84e05ce40ee2ef4d412a288c0ab2` | INVENTORIED_NOT_EXTRACTED |
| `MAESTRO_V5C_COLDSTART_BOOTSTRAP.md` | text/md | 306 | 13769 | `dc3a454c39720dccc7955afa3a3498c3349fa087facc60401ae05e1da5f1735f` | INVENTORIED_NOT_EXTRACTED |

## Trace Row Totals

- Primary trace rows: 109
- EQ-0001 segment rows: 105
- EQ-0002 member rows: 4
- EQ-0001 phrase-hit rows: 406

## Primary Trace Map Preview

| Trace ID | EQ | Element | Section/Clause | Locator | Status | Flags |
|---|---|---|---|---|---|---|
| TM-0001 | EQ-0001 | `EQ0001-S0001` | BEGIN_PREVIOUS_SESSION | lines 76-102; chars 541-25258 | SEGMENTED_NOT_SYNTHESIZED | contains_suno |
| TM-0002 | EQ-0001 | `EQ0001-S0002` | PROMPT_LABEL | lines 103-330; chars 25259-48044 | SEGMENTED_NOT_SYNTHESIZED | contains_suno |
| TM-0003 | EQ-0001 | `EQ0001-S0003` | SOURCES_LABEL | lines 331-347; chars 48045-48281 | SEGMENTED_NOT_SYNTHESIZED |  |
| TM-0004 | EQ-0001 | `EQ0001-S0004` | SOURCES_LABEL | lines 348-368; chars 48282-48776 | SEGMENTED_NOT_SYNTHESIZED |  |
| TM-0005 | EQ-0001 | `EQ0001-S0005` | SOURCES_LABEL | lines 369-387; chars 48777-49265 | SEGMENTED_NOT_SYNTHESIZED |  |
| TM-0006 | EQ-0001 | `EQ0001-S0006` | SOURCES_LABEL | lines 388-546; chars 49266-63107 | SEGMENTED_NOT_SYNTHESIZED | contains_suno |
| TM-0007 | EQ-0001 | `EQ0001-S0007` | SOURCES_LABEL | lines 547-705; chars 63108-76385 | SEGMENTED_NOT_SYNTHESIZED | contains_suno |
| TM-0008 | EQ-0001 | `EQ0001-S0008` | SOURCES_LABEL | lines 706-860; chars 76386-90161 | SEGMENTED_NOT_SYNTHESIZED | contains_suno |
| TM-0009 | EQ-0001 | `EQ0001-S0009` | SOURCES_LABEL | lines 861-864; chars 90162-90465 | SEGMENTED_NOT_SYNTHESIZED |  |
| TM-0010 | EQ-0001 | `EQ0001-S0010` | USER_SAID | lines 865-1176; chars 90466-149877 | SEGMENTED_NOT_SYNTHESIZED | contains_suno |
| TM-0011 | EQ-0001 | `EQ0001-S0011` | ASSISTANT_THOUGHT_MODEL | lines 1177-1180; chars 149878-150438 | SEGMENTED_NOT_SYNTHESIZED | contains_suno |
| TM-0012 | EQ-0001 | `EQ0001-S0012` | USER_SAID | lines 1181-1182; chars 150439-150611 | SEGMENTED_NOT_SYNTHESIZED | contains_suno |
| TM-0013 | EQ-0001 | `EQ0001-S0013` | ASSISTANT_THOUGHT_MODEL | lines 1183-1196; chars 150612-151353 | SEGMENTED_NOT_SYNTHESIZED | contains_suno |
| TM-0014 | EQ-0001 | `EQ0001-S0014` | USER_SAID | lines 1197-1234; chars 151354-155259 | SEGMENTED_NOT_SYNTHESIZED | contains_suno |
| TM-0015 | EQ-0001 | `EQ0001-S0015` | ASSISTANT_THOUGHT_MODEL | lines 1235-1282; chars 155260-157432 | SEGMENTED_NOT_SYNTHESIZED | contains_suno;contains_stop |
| TM-0016 | EQ-0001 | `EQ0001-S0016` | USER_SAID | lines 1283-1284; chars 157433-157480 | SEGMENTED_NOT_SYNTHESIZED |  |
| TM-0017 | EQ-0001 | `EQ0001-S0017` | ASSISTANT_THOUGHT_MODEL | lines 1285-1466; chars 157481-165411 | SEGMENTED_NOT_SYNTHESIZED | contains_suno |
| TM-0018 | EQ-0001 | `EQ0001-S0018` | USER_SAID | lines 1467-1468; chars 165412-165821 | SEGMENTED_NOT_SYNTHESIZED |  |
| TM-0019 | EQ-0001 | `EQ0001-S0019` | ASSISTANT_THOUGHT_MODEL | lines 1469-1486; chars 165822-167487 | SEGMENTED_NOT_SYNTHESIZED | contains_suno |
| TM-0020 | EQ-0001 | `EQ0001-S0020` | USER_SAID | lines 1487-1488; chars 167488-168103 | SEGMENTED_NOT_SYNTHESIZED | contains_file_attachment_word |
| TM-0021 | EQ-0001 | `EQ0001-S0021` | ASSISTANT_THOUGHT_MODEL | lines 1489-1520; chars 168104-171940 | SEGMENTED_NOT_SYNTHESIZED | contains_suno |
| TM-0022 | EQ-0001 | `EQ0001-S0022` | USER_SAID | lines 1521-1677; chars 171941-189099 | SEGMENTED_NOT_SYNTHESIZED | contains_suno |
| TM-0023 | EQ-0001 | `EQ0001-S0023` | USER_SAID | lines 1678-1679; chars 189100-189157 | SEGMENTED_NOT_SYNTHESIZED |  |
| TM-0024 | EQ-0001 | `EQ0001-S0024` | ASSISTANT_THOUGHT_MODEL | lines 1680-1765; chars 189158-195178 | SEGMENTED_NOT_SYNTHESIZED | contains_suno |
| TM-0025 | EQ-0001 | `EQ0001-S0025` | USER_SAID | lines 1766-1894; chars 195179-210552 | SEGMENTED_NOT_SYNTHESIZED | contains_suno |

Full primary trace map is in `TRACE_MAP_EQ0001_EQ0002.csv` and `TRACE_MAP_EQ0001_EQ0002.json`.
