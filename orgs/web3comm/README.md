<div align="center">

# web3comm · web3T

### Token · Talk · Transaction

**Wallet-to-wallet communication, where a message can carry value and a conversation can settle on chain.**

[![concept](https://img.shields.io/badge/concept-blockchain.communication-000000?style=for-the-badge)](https://github.com/Professor-Codephreak/orgmap/blob/main/ARCHIVE.md#comm)
[![forum](https://img.shields.io/badge/forum-chatter3-8338ec?style=for-the-badge)](https://github.com/chatter3)
[![chain](https://img.shields.io/badge/chain-chattchain-627EEA?style=for-the-badge)](https://github.com/chattchain)
[![standard](https://img.shields.io/badge/standard-cypherpunk4096-2ea44f?style=for-the-badge)](https://github.com/cypherpunk4096/standard)

<sub>An organization of the **[PYTHAI](https://pythai.net)** ecosystem · Platform Architect **[Professor Codephreak](https://github.com/Professor-Codephreak)**</sub>

</div>

---

## What web3comm is

web3comm is the **environment** of `blockchain.communication`: everything a wallet needs to talk to
another wallet. Its three words are its three layers.

| | Layer | The question |
|---|---|---|
| **Token** | identity and access | Who is this wallet, by name, and what does holding a token let it read or join? |
| **Talk** | the conversation | How does one wallet reach another, encrypted, without a platform in between? |
| **Transaction** | value in the message | How does a message carry a payment, a membership or a contract call? |

`blockchain.communication` is defined by two reference organizations,
**[chatter3](https://github.com/chatter3)** (the forum) and **[chattchain](https://github.com/chattchain)**
(the chain). web3comm is the wide research library around them, and
**[blktalk](https://github.com/blktalk)** is the systems layer underneath.

## Built to cypherpunk4096

web3comm follows **[cypherpunk4096](https://github.com/cypherpunk4096/standard)**, the `2¹²` standard:
verification over trust, signatures as `bytes` so the scheme can migrate (ERC-1271 for smart accounts),
one deterministic address on every chain, zero dependencies in anything meant to be permanent, and full
precision kept end to end.

## Research

Every repository here is a fork kept as **research** into its upstream's work. The upstream owns the work.

| Area | Research forks |
|---|---|
| **Token: names** (ENS) | [ens-contracts](https://github.com/web3comm/ens-contracts) · [ensjs-v3](https://github.com/web3comm/ensjs-v3) · [go-ens](https://github.com/web3comm/go-ens) · [subdomain-registrar](https://github.com/web3comm/subdomain-registrar) |
| **Token: sign-in and keys** | [sign-in-with-ethereum](https://github.com/web3comm/sign-in-with-ethereum) · [sign-in-with-web3](https://github.com/web3comm/sign-in-with-web3) · [web3auth-web](https://github.com/web3comm/web3auth-web) · [web3auth-react-native-sdk](https://github.com/web3comm/web3auth-react-native-sdk) · [single-factor-auth-web](https://github.com/web3comm/single-factor-auth-web) · [OpenLoginSdk](https://github.com/web3comm/OpenLoginSdk) · [burnmywallet](https://github.com/web3comm/burnmywallet) |
| **Token: gated access** (Lit Protocol) | [lit-js-sdk](https://github.com/web3comm/lit-js-sdk) · [js-sdk](https://github.com/web3comm/js-sdk) · [js-sdk-current](https://github.com/web3comm/js-sdk-current) · [cloudflare-litgate-js](https://github.com/web3comm/cloudflare-litgate-js) · [CeramicIntegration](https://github.com/web3comm/CeramicIntegration) · [web3.storage-lit-sdk](https://github.com/web3comm/web3.storage-lit-sdk) · [ghostshare-frontend-beta](https://github.com/web3comm/ghostshare-frontend-beta) |
| **Talk: wallet-to-wallet** (XMTP) | [xmtp-js](https://github.com/web3comm/xmtp-js) · [xmtp-inbox-web](https://github.com/web3comm/xmtp-inbox-web) · [xmtp-chat-app-nextjs](https://github.com/web3comm/xmtp-chat-app-nextjs) · [xmtp-thirdweb-js](https://github.com/web3comm/xmtp-thirdweb-js) · [awesome-xmtp](https://github.com/web3comm/awesome-xmtp) · [chat](https://github.com/web3comm/chat) · [relay](https://github.com/web3comm/relay) |
| **Talk: the Cryptoverse line** | [tokntalk](https://github.com/web3comm/tokntalk) · [ethmail.cc](https://github.com/web3comm/ethmail.cc) · [calleth.me](https://github.com/web3comm/calleth.me) · [iris](https://github.com/web3comm/iris) · [Cadbury](https://github.com/web3comm/Cadbury) |
| **Talk: the networks people already use** | [tdesktop](https://github.com/web3comm/tdesktop) (Telegram) · [Rooster](https://github.com/web3comm/Rooster) · [Android-XMPP](https://github.com/web3comm/Android-XMPP) · [twitter.js](https://github.com/web3comm/twitter.js) · [node-twitter-api-v2](https://github.com/web3comm/node-twitter-api-v2) · [Twitter-API-v2-sample-code](https://github.com/web3comm/Twitter-API-v2-sample-code) · [tweet-json-to-html](https://github.com/web3comm/tweet-json-to-html) · [react-tweet-embed](https://github.com/web3comm/react-tweet-embed) · [react-twitter-embed](https://github.com/web3comm/react-twitter-embed) · [react-twitter-widgets](https://github.com/web3comm/react-twitter-widgets) · [react-social-login](https://github.com/web3comm/react-social-login) · [my-auth-app](https://github.com/web3comm/my-auth-app) · [counterfacto](https://github.com/web3comm/counterfacto) |
| **Transaction: value in the message** | [DeChat](https://github.com/web3comm/DeChat) (send tokens in chat) · [unlock](https://github.com/web3comm/unlock) (memberships) · [frame](https://github.com/web3comm/frame) · [rainbowkit](https://github.com/web3comm/rainbowkit) · [wagmi](https://github.com/web3comm/wagmi) · [js](https://github.com/web3comm/js) (thirdweb) |
| **Clients and proofs** | [web3j](https://github.com/web3comm/web3j) (Java/Android) · [KEthereum](https://github.com/web3comm/KEthereum) (Kotlin) · [wasmsnark](https://github.com/web3comm/wasmsnark) · [hammer.js](https://github.com/web3comm/hammer.js) |
| **Agents and voice** | [agent-skills](https://github.com/web3comm/agent-skills) · [awesome-agent-skills](https://github.com/web3comm/awesome-agent-skills) · [awesome-openclaw-skills](https://github.com/web3comm/awesome-openclaw-skills) · [nano-banana-pro-prompts-recommend-skill](https://github.com/web3comm/nano-banana-pro-prompts-recommend-skill) · [open-claude-cowork](https://github.com/web3comm/open-claude-cowork) · [ComfyUI-Qwen-TTS](https://github.com/web3comm/ComfyUI-Qwen-TTS) · [ComfyUI-FL-Qwen3TTS](https://github.com/web3comm/ComfyUI-FL-Qwen3TTS) |

## Status

web3comm is research. Nothing has been released or deployed under this organization. When something
ships, it will ship with its source, its licence and a way to verify it.

## The estate

| | |
|---|---|
| **[chatter3](https://github.com/chatter3)** · **[chattchain](https://github.com/chattchain)** | the forum and the chain: the reference for `blockchain.communication` |
| **[blktalk](https://github.com/blktalk)** | the systems layer: zero knowledge, subnets, bridges, identity |
| **[blockwhisper](https://github.com/blockwhisper)** | the continuation of `blockchain.communication`: the public [working record](https://github.com/blockwhisper/blockchain.communication) and what comes next |
| **[cypherpunk4096](https://github.com/cypherpunk4096)** | the standard |
| **[cryptoAGI](https://github.com/cryptoAGI)** | the agents that take part |
| **[orgmap](https://github.com/Professor-Codephreak/orgmap)** | the map of the whole estate |

<div align="center">

**Code is law. Keys are identity. Verification replaces trust.**

</div>
