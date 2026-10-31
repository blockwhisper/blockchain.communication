# Continuation — blockchain.communication

Read this first if you are picking the work up, whether you are a person or an agent. It states what
exists, where it lives, what is done, what is waiting and on whom, and the rules the work follows.
State as of **2026-10-29**. GitHub is the live record. Where this file and GitHub disagree, GitHub is
right and this file gets fixed.

## The concept

**`blockchain.communication`**: wallet-to-wallet messaging where a message is trusted because its
signature verifies, not because of the account that sent it or the server that stored it. It is the
`comm` domain of the estate map, [Professor-Codephreak/orgmap](https://github.com/Professor-Codephreak/orgmap)
(`domains.json`, `ARCHIVE.md#comm`).

| Org | Kind in orgmap | Role | Owner | Professor-Codephreak |
|---|---|---|---|---|
| [chatter3](https://github.com/chatter3) | reference | **the forum**: signature-verified conversation for people and agents | THRUSTDeltaV | member |
| [chattchain](https://github.com/chattchain) | reference | **the chain**: messages and identity carried on chain | THRUSTDeltaV | member (admin on `.github`) |
| [web3comm](https://github.com/web3comm) | role | **the environment**: Token · Talk · Transaction | Professor-Codephreak | owner |
| [blktalk](https://github.com/blktalk) | role | **the systems layer**: Proof · Place · Passage · Person | THRUSTDeltaV | member |
| [blockwhisper](https://github.com/blockwhisper) | role | **the continuation**: this repository | Professor-Codephreak | owner |

Note the spelling **chattchain** (two t's). `github.com/chatchain` is an unrelated, empty user account
from 2016.

The estate around it:

| | |
|---|---|
| [cypherpunk4096](https://github.com/cypherpunk4096) | the standard every org here is built to: determinism as identity, zero dependencies, verification over trust (the green checkmark), precision without approximation, quantum compliance (signatures as `bytes`, ERC-1271, migration behind a timelock) |
| [cryptoAGI](https://github.com/cryptoAGI) | the agents that take part: sagi/Savante (signed verdicts), bankml (a receipt on every answer), voaice/voaicers/streamair (voice), jaimla/luvai (the facet-bundle lineage) |
| [orgmap](https://github.com/Professor-Codephreak/orgmap) | the map of the whole estate; local tree `~/orgmap` |
| [PYTHAI](https://pythai.net) · [AgenticPlace](https://agenticplace.pythai.net) · [mindX](https://mindx.pythai.net) · [BANKON](https://bankon.pythai.net) · [rage](https://rage.pythai.net) | the ecosystem the orgs credit |

## What is in this repository

| Path | What |
|---|---|
| `orgs/<org>/README.md` | the org landing (`.github/profile/README.md`) written for each of the four orgs, as committed |
| `icon/chatter3-gold.png` | chatter3's coin icon: transparent background, shiny silver-gold edge (460 × 460, the largest size GitHub serves) |
| `icon/chatter3-transparent.png` | the same, original blue edge |
| `icon/avatar-original.jpg` | chatter3's avatar as it is on GitHub today |
| `icon/transp.py` · `icon/gold.py` | the two steps that made the icon: flood-fill the white background from the edges to transparent; recolour only the blue band connected to the outside (never the slate face panel) to silver-gold |

## Done

| Where | What | Commit |
|---|---|---|
| chattchain/.github | landing rewritten as *the chain*; all 19 research forks by question; blockwhisper added | `750cde9`, `0657359` (pushed) |
| web3comm/.github | landing rewritten as Token · Talk · Transaction; all 60 forks by layer; blockwhisper added | `c06dfed`, `68b3473` (pushed) |
| orgmap | Communication named `blockchain.communication`; `reference` chatter3 + chattchain | `4ed956c` (pushed) |
| orgmap | `roles` for web3comm and blktalk | `be285eb` (pushed) |
| orgmap | `descriptions` overrides for chatter3 (GitHub has only a motto) and chattchain (GitHub has none) | `1785943` (pushed) |
| blockwhisper/.github | public org landing: the five parts, cypherpunk4096, cryptoAGI | `044e3b8` (pushed) |
| blockwhisper/blockchain.communication | this repository (created private, made public 2026-10-29 on the operator's instruction) | `c48df2b` (pushed) |
| orgmap | blockwhisper filed in `comm` with a role and description; 100 organizations, 4,990 repositories | `819e9c5` (pushed) |

## Waiting — and on whom

Everything below needs the **THRUSTDeltaV** account, the only owner of chatter3, chattchain and blktalk.

| # | Org | Waiting | How |
|---|---|---|---|
| 1 | chatter3 | landing `e78b4f4` + `f22df11` (adds blockwhisper and chattchain) | push from a clone with THRUSTDeltaV's credentials, or copy `orgs/chatter3/README.md` to `chatter3/.github` → `profile/README.md` |
| 2 | blktalk | landing `8c8abe7` + `06a3981` (adds blockwhisper) | the same, from `orgs/blktalk/README.md` |
| 3 | chatter3 | gold icon | <https://github.com/organizations/chatter3/settings/profile> → Upload new picture → `icon/chatter3-gold.png`, keep the full crop. GitHub has no API for org avatars |
| 4 | chattchain | org description | same settings page for chattchain. Text: *blockchain.communication — the chain: messages and identity carried on chain, verified by signature. Research into XMTP, on-chain inboxes, DIDs and encrypted memos.* |
| 5 | chatter3 | org description (optional) | text: *blockchain.communication — the forum: signature-verified conversation for people and agents* |

The alternative to all five: THRUSTDeltaV makes Professor-Codephreak an owner of the three orgs.
After 4 and 5, re-fetch orgmap and remove the `descriptions` overrides in `domains.json`, so GitHub is
the single source.

## Next

- **orgmap's next full re-fetch** (`fetch.py`, `fetch_detail.py`, `fetch_readme.py`, then
  `generate.py`) picks blockwhisper up in the normal way. On 2026-10-29 it was added to the
  git-ignored `data.json` for this org alone, so `detail.json` and `readme.json` have nothing for it yet.
- **Nothing has shipped** under any of the five orgs. The forum in chatter3 is research (a fork of
  the XMTP web UI). The first shipped unit should carry the cypherpunk4096 mark from the start:
  client-side signing and verification (CAIP-122 / SIWE, EOA + ERC-1271 + ERC-6492), signatures as
  `bytes`, zero dependencies on the signing path, source verified on a public explorer.
- **`cypherpunk4096/login333`** is the planned zero-dependency client-side login and green-checkmark
  minter. As of 2026-10-29 it is **not on GitHub**. Don't link it or describe it as published until it is.

## Rules

- **Forks are research.** Every fork studies its upstream, and the upstream owns the work. Never call
  them bare forks, and credit the upstream.
- **Say what is true.** Every landing ends with a status that says nothing has shipped. Keep it that
  way until something does.
- **Private until release** for new working repositories (this one was, until the operator made it public on 2026-10-29). Org landings in
  `.github` must be public for GitHub to show them.
- **Commits** are authored as `codephreak <codephreak@dmg.finance>` and end with
  `Co-Authored-By: Professor Codephreak <codephreak@pythai.net>`. Stage explicit files and check
  the staged set for secrets before committing.
- **Licences:** client-side crypto and key code `GPL-3.0-only OR Apache-2.0`, backend MIT, per path,
  SPDX header authoritative (the BANKON tri-licence; precedent `cypherpunk4096/BANKONBTCWaaS`).
