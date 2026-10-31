<div align="center">

# blktalk

### `blockchain.communication` — the systems layer

**Wallet-signature communication, and the machinery underneath it: proofs, subnets, bridges and identity.**

[![concept](https://img.shields.io/badge/concept-blockchain.communication-000000?style=for-the-badge)](https://github.com/Professor-Codephreak/orgmap/blob/main/ARCHIVE.md#comm)
[![forum](https://img.shields.io/badge/forum-chatter3-8338ec?style=for-the-badge)](https://github.com/chatter3)
[![chain](https://img.shields.io/badge/chain-chattchain-627EEA?style=for-the-badge)](https://github.com/chattchain)
[![standard](https://img.shields.io/badge/standard-cypherpunk4096-2ea44f?style=for-the-badge)](https://github.com/cypherpunk4096/standard)

<sub>An organization of the **[PYTHAI](https://pythai.net)** ecosystem · Platform Architect **[Professor Codephreak](https://github.com/Professor-Codephreak)**</sub>

</div>

---

## What blktalk is

blktalk is research into **wallet-based signature communication**: one wallet speaking directly to
another, every message signed, nothing in the middle that has to be trusted.

In `blockchain.communication`, **[chatter3](https://github.com/chatter3)** is the forum,
**[chattchain](https://github.com/chattchain)** is the chain, and **[web3comm](https://github.com/web3comm)**
is the wide environment of Token · Talk · Transaction. blktalk goes underneath them all, to the
systems a conversation stands on:

- **Proof:** saying something true without revealing more than you must (zero knowledge).
- **Place:** networks a community can spawn for itself, with their own rules and consensus (subnets).
- **Passage:** moving messages and value between chains (bridges).
- **Person:** an identity a key controls, with names and credentials it can carry anywhere.

## Built to cypherpunk4096

blktalk follows **[cypherpunk4096](https://github.com/cypherpunk4096/standard)**, the `2¹²` standard:
verification over trust, signatures as `bytes` so the scheme can migrate (ERC-1271 for smart accounts),
one deterministic address on every chain, zero dependencies in anything meant to be permanent, and full
precision kept end to end.

## Research

Every repository here is a fork kept as **research** into its upstream's work. The upstream owns the work.

| Area | Research forks |
|---|---|
| **Proof** (zero knowledge) | [zk-kit](https://github.com/blktalk/zk-kit) · [zk-kit.solidity](https://github.com/blktalk/zk-kit.solidity) · [zkp-app-boilerplate](https://github.com/blktalk/zkp-app-boilerplate) · [snark-artifacts](https://github.com/blktalk/snark-artifacts) · [zkey-manager](https://github.com/blktalk/zkey-manager) · [zkevm-docs](https://github.com/blktalk/zkevm-docs) |
| **Place** (Interplanetary Consensus subnets) | [ipc](https://github.com/blktalk/ipc) · [ipc-atomic-execution](https://github.com/blktalk/ipc-atomic-execution) · [ipc-bridge](https://github.com/blktalk/ipc-bridge) · [fendermint](https://github.com/blktalk/fendermint) · [spacenet](https://github.com/blktalk/spacenet) · [consensus-factory](https://github.com/blktalk/consensus-factory) · [icpdocs](https://github.com/blktalk/icpdocs) |
| **Passage** (bridges) | [zkevm-contracts](https://github.com/blktalk/zkevm-contracts) (AggLayer) · [zkevm-bridge-ui](https://github.com/blktalk/zkevm-bridge-ui) |
| **Person** (identity and names) | [did-eth](https://github.com/blktalk/did-eth) · [ethr-did-registry](https://github.com/blktalk/ethr-did-registry) · [uns](https://github.com/blktalk/uns) · [sign-in-with-web3](https://github.com/blktalk/sign-in-with-web3) · [web3auth-web](https://github.com/blktalk/web3auth-web) · [OpenLoginSdk](https://github.com/blktalk/OpenLoginSdk) · [ethjs-signer](https://github.com/blktalk/ethjs-signer) |
| **The conversation** (XMTP, WalletConnect) | [libxmtp](https://github.com/blktalk/libxmtp) · [xmtpd](https://github.com/blktalk/xmtpd) · [xmtp-js](https://github.com/blktalk/xmtp-js) · [xmtp-web](https://github.com/blktalk/xmtp-web) · [xmtp-inbox-web](https://github.com/blktalk/xmtp-inbox-web) · [xmtp-message-history-server](https://github.com/blktalk/xmtp-message-history-server) · [relay](https://github.com/blktalk/relay) · [blocktalk](https://github.com/blktalk/blocktalk) (Tokntalk) · [ethmail.cc](https://github.com/blktalk/ethmail.cc) · [calleth.me](https://github.com/blktalk/calleth.me) |
| **Private access** (Lit Protocol, secrets) | [lit-js-sdk](https://github.com/blktalk/lit-js-sdk) · [js-lit-sdk](https://github.com/blktalk/js-lit-sdk) · [web3.storage-lit-sdk](https://github.com/blktalk/web3.storage-lit-sdk) · [ghostshare-frontend-beta](https://github.com/blktalk/ghostshare-frontend-beta) · [secrets](https://github.com/blktalk/secrets) |
| **Social wallets** (dyne.org) | [social-wallet-api](https://github.com/blktalk/social-wallet-api) · [social-wallet-admin-console](https://github.com/blktalk/social-wallet-admin-console) · [socialwallet.app](https://github.com/blktalk/socialwallet.app) · [dynebot](https://github.com/blktalk/dynebot) · [SocialTokens](https://github.com/blktalk/SocialTokens) · [unlock](https://github.com/blktalk/unlock) |
| **Tools** | [smart-contract-registry](https://github.com/blktalk/smart-contract-registry) · [serialTerminal.com](https://github.com/blktalk/serialTerminal.com) · [broh5](https://github.com/blktalk/broh5) · [express-file-handling](https://github.com/blktalk/express-file-handling) · [cryptolot](https://github.com/blktalk/cryptolot) |

## Status

blktalk is research. Nothing has been released or deployed under this organization. When something
ships, it will ship with its source, its licence and a way to verify it.

## The estate

| | |
|---|---|
| **[chatter3](https://github.com/chatter3)** · **[chattchain](https://github.com/chattchain)** | the forum and the chain: the reference for `blockchain.communication` |
| **[web3comm](https://github.com/web3comm)** | Token · Talk · Transaction: the communication environment |
| **[blockwhisper](https://github.com/blockwhisper)** | the continuation of `blockchain.communication`: the public [working record](https://github.com/blockwhisper/blockchain.communication) and what comes next |
| **[cypherpunk4096](https://github.com/cypherpunk4096)** | the standard |
| **[cryptoAGI](https://github.com/cryptoAGI)** | the agents that take part |
| **[orgmap](https://github.com/Professor-Codephreak/orgmap)** | the map of the whole estate |

<div align="center">

**Code is law. Keys are identity. Verification replaces trust.**

</div>
