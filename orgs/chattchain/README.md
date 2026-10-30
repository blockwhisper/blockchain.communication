<div align="center">

# chattchain

### `blockchain.communication` — the chain

**Messages and identity carried on chain. A message is trusted because its signature verifies.**

[![concept](https://img.shields.io/badge/concept-blockchain.communication-000000?style=for-the-badge)](https://github.com/Professor-Codephreak/orgmap/blob/main/ARCHIVE.md#comm)
[![forum](https://img.shields.io/badge/forum-chatter3-8338ec?style=for-the-badge)](https://github.com/chatter3)
[![standard](https://img.shields.io/badge/standard-cypherpunk4096-2ea44f?style=for-the-badge)](https://github.com/cypherpunk4096/standard)

<sub>An organization of the **[PYTHAI](https://pythai.net)** ecosystem · Platform Architect **[Professor Codephreak](https://github.com/Professor-Codephreak)**</sub>

</div>

---

## What chattchain is

`blockchain.communication` has two reference organizations. **[chatter3](https://github.com/chatter3)**
is the forum: signature-verified conversation for people and agents. **chattchain** is the chain
underneath it: where a message, an inbox and an identity live once they leave the forum's screen.

The questions chattchain studies are the ones a signed conversation has to answer on chain:

- **Who is speaking?** An identity a key controls, resolvable without asking a platform.
- **Where does a message go?** An inbox addressed by a hash, not by a server's account table.
- **What can be kept private?** Encrypted memos riding with a payment, readable only by the parties.
- **What must be kept forever?** Permanent storage for the record that should outlive its host.

## Built to cypherpunk4096

chattchain follows **[cypherpunk4096](https://github.com/cypherpunk4096/standard)**, the `2¹²` standard:
verification over trust, signatures as `bytes` so the scheme can migrate (ERC-1271 for smart
accounts), one deterministic address on every chain, zero dependencies in anything meant to be
permanent, and full precision kept end to end.

## Research

Every repository here is a fork kept as **research** into its upstream's work. The upstream owns the work.

| Question | Research fork | Studies |
|---|---|---|
| **Inbox on chain** | [conversation-contract](https://github.com/chattchain/conversation-contract) | a contract that sends messages to an inbox identified by a conversation hash |
| **The message network** | [xmtpd](https://github.com/chattchain/xmtpd) · [xmtp-js](https://github.com/chattchain/xmtp-js) · [xmtp-js-content-types](https://github.com/chattchain/xmtp-js-content-types) · [xmtp-message-history-server](https://github.com/chattchain/xmtp-message-history-server) · [xmtp-quickstart-node](https://github.com/chattchain/xmtp-quickstart-node) · [xmtp-quickstart-node-groups](https://github.com/chattchain/xmtp-quickstart-node-groups) · [xmtp-quickstart-request-inbox](https://github.com/chattchain/xmtp-quickstart-request-inbox) | XMTP: the node, the client SDK, content types, history sync and group chat |
| **Identity** | [ethr-did-registry](https://github.com/chattchain/ethr-did-registry) | ERC-1056 decentralized identifiers on Ethereum |
| **Private memos with value** | [recibo](https://github.com/chattchain/recibo) | encrypted memos attached to ERC-20 transfers |
| **Other execution models** | [motoko](https://github.com/chattchain/motoko) · [motoko-core](https://github.com/chattchain/motoko-core) | Internet Computer canisters and their standard library |
| **Permanence** | [ar-io-deploy](https://github.com/chattchain/ar-io-deploy) | deploying to Arweave and pointing an ArNS name at it |
| **Federated social** | [gnu-social](https://github.com/chattchain/gnu-social) | GNU social, the free-software federated network |
| **Building the dapp** | [scaffold-eth-2](https://github.com/chattchain/scaffold-eth-2) · [dappchainkit](https://github.com/chattchain/dappchainkit) | an Ethereum dev stack; on-chain React components |
| **The forum and the field** | [chatter3](https://github.com/chattchain/chatter3) · [DeltaVerse](https://github.com/chattchain/DeltaVerse) | the chatter3 XMTP web UI; DeltaVerse self-verifying NFTs |
| **Writing it down** | [Markdown-Cheatsheet](https://github.com/chattchain/Markdown-Cheatsheet) | Markdown reference |

## Status

chattchain is research. Nothing has been released or deployed under this organization. When something
ships, it will ship with its source, its licence and a way to verify it.

## The estate

| | |
|---|---|
| **[chatter3](https://github.com/chatter3)** | the forum — the other half of `blockchain.communication` |
| **[blktalk](https://github.com/blktalk)** · **[web3comm](https://github.com/web3comm)** | wallet-signature communication research |
| **[blockwhisper](https://github.com/blockwhisper)** | the continuation of `blockchain.communication`: the public [working record](https://github.com/blockwhisper/blockchain.communication) and what comes next |
| **[cypherpunk4096](https://github.com/cypherpunk4096)** | the standard |
| **[cryptoAGI](https://github.com/cryptoAGI)** | the agents that take part |
| **[orgmap](https://github.com/Professor-Codephreak/orgmap)** | the map of the whole estate |

<div align="center">

**Code is law. Keys are identity. Verification replaces trust.**

</div>
