<div align="center">

# Crypto Top Papers

**Cryptocurrency, blockchain and Web3 papers at CS top conferences**

NeurIPS · ICML · ICLR · KDD · WWW · AAAI · IJCAI · CIKM · ICDM · ICDE · SIGIR · WSDM · ACL · EMNLP

![Papers](https://img.shields.io/badge/papers-160-blue) ![With Code](https://img.shields.io/badge/with%20code-30-blueviolet) ![Updated](https://img.shields.io/badge/updated-2026--10--04-green) [![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

</div>

# About

A curated list of **peer-reviewed** papers on cryptocurrency, blockchain and Web3 from 14 CS top conferences (2024–2026), with links to each paper and its code.

- **Continuously updated.** New papers are added as each conference publishes its proceedings (see [Updates](#updates)).
- **Easy to scan.** Each paper is listed once under its main task, with method tags such as `GNN`, `LLM` and `RL` and chain tags such as *Bitcoin* and *Ethereum*. ＊ marks a general financial method that uses crypto data as a main dataset.

Feel free to suggest decent papers via a PR (see [How to Contribute](#how-to-contribute)). If you find this repository helpful, consider leaving a ⭐

# Table of Contents

- [About](#about)
- [Venue Statistics](#venue-statistics)
- [Papers by Task](#papers-by-task)
  - [Price Forecasting & Market Analysis](#price-forecasting--market-analysis) (11)
  - [Trading & Portfolio Management](#trading--portfolio-management) (17)
  - [Fraud, Scam & Attack Detection](#fraud-scam--attack-detection) (22)
  - [On-chain Transaction & Graph Analytics](#on-chain-transaction--graph-analytics) (16)
  - [DeFi, MEV & Market Mechanisms](#defi-mev--market-mechanisms) (11)
  - [NFT, DAO & Web3 Ecosystem](#nft-dao--web3-ecosystem) (17)
  - [Smart Contract Security & Analysis](#smart-contract-security--analysis) (19)
  - [Blockchain Systems & Infrastructure](#blockchain-systems--infrastructure) (39)
  - [Surveys, Tutorials & Workshops](#surveys-tutorials--workshops) (8)
- [Papers by Year](#papers-by-year)
  - [2026](#2026)
  - [2025](#2025)
  - [2024](#2024)
- [Datasets & Benchmarks](#datasets--benchmarks) (11)
- [How to Contribute](#how-to-contribute)
- [License](#license)

# Venue Statistics

| Venue | 2024 | 2025 | 2026 | Total |
|:--|:-:|:-:|:-:|:-:|
| NeurIPS | 2 | 5 | 6 | 13 |
| ICML | – | 1 | 2 | 3 |
| ICLR | 1 | 2 | 3 | 6 |
| KDD | 5 | 4 | 3 | 12 |
| WWW | 29 | 18 | 23 | 70 |
| AAAI | 2 | 3 | 4 | 9 |
| IJCAI | 3 | 3 | 2 | 8 |
| CIKM | 3 | 3 | – | 6 |
| ICDM | – | 2 | – | 2 |
| ICDE | 10 | 6 | 9 | 25 |
| SIGIR | – | – | 1 | 1 |
| WSDM | – | 1 | – | 1 |
| ACL | – | – | 2 | 2 |
| EMNLP | 1 | 1 | – | 2 |
| **Total** | **56** | **49** | **55** | **160** |

# Papers by Task

## Price Forecasting & Market Analysis

*Price, return and volatility forecasting, market simulation, and event or news analysis.*

- (NeurIPS 2026) **Generating Financial Time Series by Matching Random Convolutional Features** ＊ [[Paper](https://openreview.net/forum?id=tLVW1Y9hBz)] `Generative` `Time-Series` · *Crypto*
- (ICLR 2026) **CTBench: Cryptocurrency Time Series Generation Benchmark** [[Paper](https://openreview.net/forum?id=RzT2sombPD)] `Generative` `Time-Series` · *Crypto*
- (ICLR 2026 Workshop) **Probabilistic Multivariate Time Series Forecasting with Diffusion Copulas** [[Paper](https://arxiv.org/abs/2605.19685)] `Diffusion` `Time-Series` · *Crypto*
- (KDD 2026) **Towards Event-Aware Forecasting in DeFi: Insights from On-chain Automated Market Maker Protocols** [[Paper](https://doi.org/10.1145/3770855.3817502)] [[Code](https://github.com/finbrain-lab-hkustgz/Deep-AMM-Events)] `Time-Series` · *DEX*
- (AAAI 2026) **Market-Aware Event Timeline Summarization: Integrating Price Signals to Improve Financial News Understanding** [[Paper](https://doi.org/10.1609/aaai.v40i48.42370)] `LLM` `NLP` · *Crypto*
- (ICLR 2025 Workshop) **FinTSBridge: A New Evaluation Suite for Real-world Financial Prediction with Advanced Time Series Models** ＊ [[Paper](https://arxiv.org/abs/2503.06928)] `Time-Series` · *Crypto*
- (KDD 2025) **CryptoMixer: Fine-grained market information-aware MLP Networks for Individual Cryptocurrency Trading Prediction** [[Paper](https://doi.org/10.1145/3711896.3736900)] [[Code](https://github.com/aqua111000/CryptoMixer)] `MLP` `Time-Series` · *Crypto*
- (CIKM 2025) **From Patterns to Predictions: A Shapelet-Based Framework for Directional Forecasting in Noisy Financial Markets** ＊ [[Paper](https://doi.org/10.1145/3746252.3761250)] `Shapelet` `Time-Series` · *Bitcoin*
- (KDD 2024) **COMET: NFT Price Prediction with Wallet Profiling** [[Paper](https://doi.org/10.1145/3637528.3671621)] `Time-Series` `Graph` · *NFT*
- (IJCAI 2024) **Trade When Opportunity Comes: Price Movement Forecasting via Locality-Aware Attention and Iterative Refinement Labeling** ＊ [[Paper](https://doi.org/10.24963/ijcai.2024/678)] `Transformer` · *Crypto*
- (CIKM 2024) **Cryptocurrency Price Forecasting using Variational Autoencoder with Versatile Quantile Modeling** [[Paper](https://doi.org/10.1145/3627673.3680027)] `Generative` `Time-Series` · *Crypto*

## Trading & Portfolio Management

*RL and LLM trading agents, high-frequency trading, portfolio management and arbitrage.*

- (NeurIPS 2026) **Market Regime Council for Dynamic Credit Assignment in Multi-Agent LLM Decision Systems** [[Paper](https://openreview.net/forum?id=xuhyMmn0D0)] `LLM` `Agent` · *Crypto*
- (ICLR 2026) **Trade in Minutes! Rationality-Driven Agentic System for Quantitative Financial Trading** ＊ [[Paper](https://openreview.net/forum?id=ROEwZAxqyS)] `LLM` `Agent` · *Crypto*
- (KDD 2026) **FineFT: Efficient and Risk-Aware Ensemble Reinforcement Learning for Futures Trading** [[Paper](https://doi.org/10.1145/3770854.3780187)] `RL` · *Crypto*
- (WWW 2026) **Analysis of CEX-DEX Arbitrage Opportunities with Hidden Markov Models** [[Paper](https://doi.org/10.1145/3774904.3792185)] `HMM` · *DEX*
- (WWW 2026) **Resisting Manipulative Bots in Meme Coin Copy Trading: A Multi-Agent Approach with Chain-of-Thought Reasoning** [[Paper](https://arxiv.org/abs/2601.08641)] `LLM` `Multi-Agent` · *Memecoin*
- (WWW 2026 Companion) **Learning-Based Optimization of Atomic Arbitrage in Decentralized Financial Systems** [[Paper](https://doi.org/10.1145/3774905.3794707)] `Optimization` · *DEX*
- (AAAI 2026) **ArchetypeTrader: Reinforcement Learning for Selecting and Refining Learnable Strategic Archetypes in Quantitative Trading** [[Paper](https://doi.org/10.1609/aaai.v40i34.40166)] [[Code](https://github.com/yfcck/ArchetypeTrader)] `RL` · *Crypto*
- (ICDE 2026) **TRADER: Real-time Arbitrage Detection via Negative Cycles on Dynamic Graphs** [[Paper](https://doi.org/10.1109/icde65706.2026.00141)] `Graph-Algorithms` · *DEX*
- (NeurIPS 2025) **OPHR: Mastering Volatility Trading with Multi-Agent Deep Reinforcement Learning** [[Paper](https://openreview.net/forum?id=2p4AtivyZz)] [[Code](https://github.com/Edwicn/OPHR-MasteringVolatilityTradingwithMultiAgentDeepReinforcementLearning)] `RL` `Multi-Agent` · *Bitcoin, Ethereum*
- (NeurIPS 2025 Workshop) **Orchestration Framework for Financial Agents: From Algorithmic Trading to Agentic Trading** ＊ [[Paper](https://arxiv.org/abs/2512.02227)] [[Code](https://github.com/Open-Finance-Lab/AgenticTrading)] `LLM` `Agent` · *Crypto*
- (ICML 2025) **Pareto-Optimality, Smoothness, and Stochasticity in Learning-Augmented One-Max-Search** ＊ [[Paper](https://openreview.net/forum?id=ZTOVlPC5Vf)] `Online-Algorithms` · *Bitcoin*
- (ICLR 2025 Workshop) **Exploring LLM Cryptocurrency Trading Through Fact-Subjectivity Aware Reasoning** [[Paper](https://arxiv.org/abs/2410.12464)] [[Code](https://github.com/HaeSe0ng/FS-ReasoningAgent)] `LLM` · *Crypto*
- (WWW 2025 Companion) **HedgeAgents: A Balanced-aware Multi-agent Financial Trading System** ＊ [[Paper](https://doi.org/10.1145/3701716.3715232)] [[Code](https://github.com/hedgeagents/hedgeagents.github.io)] `LLM` `Agent` · *Crypto*
- (CIKM 2025) **Adaptive Bidirectional State Space Model for High-frequency Portfolio Management** ＊ [[Paper](https://doi.org/10.1145/3746252.3761246)] `SSM` `RL` · *Crypto*
- (KDD 2024) **MacroHFT: Memory Augmented Context-aware Reinforcement Learning On High Frequency Trading** [[Paper](https://doi.org/10.1145/3637528.3672064)] [[Code](https://github.com/ZONG0004/MacroHFT)] `RL` · *Crypto*
- (AAAI 2024) **EarnHFT: Efficient Hierarchical Reinforcement Learning for High Frequency Trading** [[Paper](https://doi.org/10.1609/aaai.v38i13.29384)] [[Code](https://github.com/TradeMaster-NTU/EarnHFT)] `RL` · *Crypto*
- (EMNLP 2024) **CryptoTrade: A Reflective LLM-based Agent to Guide Zero-shot Cryptocurrency Trading** [[Paper](https://doi.org/10.18653/v1/2024.emnlp-main.63)] [[Code](https://github.com/Xtra-Computing/CryptoTrade)] `LLM` `Agent` · *Crypto*

## Fraud, Scam & Attack Detection

*Phishing, scams, rug pulls, money laundering, wash trading, bots and attack transactions.*

- (ICML 2026) **Scam2Prompt: A Scalable Framework for Auditing Malicious Scam Endpoints in Production LLMs** ＊ [[Paper](https://openreview.net/forum?id=jEQQBE30m1)] [[Code](https://github.com/Scam2Prompt/Scam2Prompt)] `LLM` · *Web3*
- (WWW 2026) **Evasion Under Blockchain Sanctions** [[Paper](https://doi.org/10.1145/3774904.3792715)] `Measurement` · *Ethereum*
- (WWW 2026) **Multi-Modal Enhanced Graph Transfer Learning for Digital Finance Fraud Detection** [[Paper](https://doi.org/10.1145/3774904.3792946)] `GNN` `Multimodal` `Transfer-Learning` · *Crypto*
- (WWW 2026) **Understanding Post-Exploit Laundering Behavior on Ethereum** [[Paper](https://doi.org/10.1145/3774904.3792918)] `Measurement` · *Ethereum*
- (IJCAI 2026) **Temporal Motif-aware Graph Test-time Adaptation for OOD Blockchain Anomaly Detection** [[Paper](https://doi.org/10.24963/ijcai.2026/802)] [[Code](https://github.com/LuoXishuang0712/TEMG-TTA)] `GNN` `Temporal-Graph` · *Crypto*
- (SIGIR 2026) **TDHGNN: A Temporal Directed Hypergraph Neural Network for Bitcoin Fraud Detection** [[Paper](https://doi.org/10.1145/3805712.3809899)] [[Code](https://github.com/KellyGong/TDHGNN)] `Hypergraph` `Temporal-Graph` · *Bitcoin*
- (NeurIPS 2025) **BlockScan: Detecting Anomalies in Blockchain Transactions** [[Paper](https://openreview.net/forum?id=URB690A5r5)] `Transformer` `LLM` · *Crypto*
- (KDD 2025) **TEMPER: Capturing Consistent and Fluctuating TEMPoral User Behaviour for EtheReum Phishing Scam Detection** [[Paper](https://doi.org/10.1145/3690624.3709399)] `Temporal-Graph` · *Ethereum*
- (WWW 2025) **CATALOG: Exploiting Joint Temporal Dependencies for Enhanced Phishing Detection on Ethereum** [[Paper](https://doi.org/10.1145/3696410.3714903)] `Temporal-Graph` · *Ethereum*
- (WWW 2025) **Hunting in the Dark Forest: A Pre-trained Model for On-chain Attack Transaction Detection in Web3** [[Paper](https://doi.org/10.1145/3696410.3714928)] [[Code](https://github.com/wuzhy1ng/attack_trans_detection_www25)] `Pre-training` `Transformer` · *EVM*
- (WWW 2025) **Safeguarding Blockchain Ecosystem: Understanding and Detecting Attack Transactions on Cross-chain Bridges** [[Paper](https://doi.org/10.1145/3696410.3714604)] `Measurement` · *Cross-chain*
- (WWW 2025) **Serial Scammers and Attack of the Clones: How Scammers Coordinate Multiple Rug Pulls on Decentralized Exchanges** [[Paper](https://doi.org/10.1145/3696410.3714919)] `Measurement` · *DEX*
- (WWW 2025) **The Poorest Man in Babylon: A Longitudinal Study of Cryptocurrency Investment Scams** [[Paper](https://doi.org/10.1145/3696410.3714588)] `Measurement` · *Crypto*
- (WWW 2024) **ARTEMIS: Detecting Airdrop Hunters in NFT Markets with a Graph Learning System** [[Paper](https://doi.org/10.1145/3589334.3645597)] `GNN` · *NFT*
- (WWW 2024) **DenseFlow: Spotting Cryptocurrency Money Laundering in Ethereum Transaction Graphs** [[Paper](https://doi.org/10.1145/3589334.3645692)] `Graph-Mining` · *Ethereum*
- (WWW 2024) **Identifying Risky Vendors in Cryptocurrency P2P Marketplaces** [[Paper](https://doi.org/10.1145/3589334.3645475)] `Machine-Learning` · *Crypto*
- (WWW 2024) **Interface Illusions: Uncovering the Rise of Visual Scams in Cryptocurrency Wallets** [[Paper](https://doi.org/10.1145/3589334.3645348)] `Measurement` · *Wallet*
- (WWW 2024) **ZipZap: Efficient Training of Language Models for Large-Scale Fraud Detection on Blockchain** [[Paper](https://doi.org/10.1145/3589334.3645352)] [[Code](https://github.com/git-disl/ZipZap)] `Transformer` `Pre-training` · *Ethereum*
- (WWW 2024 Companion) **Detecting Financial Bots on the Ethereum Blockchain** [[Paper](https://doi.org/10.1145/3589335.3651959)] `Machine-Learning` · *Ethereum*
- (WWW 2024 Companion) **Towards Understanding Crypto-Asset Risks on Ethereum Caused by Key Leakage on the Internet** [[Paper](https://doi.org/10.1145/3589335.3651573)] `Measurement` · *Ethereum*
- (WWW 2024 Companion) **Unveiling Wash Trading in Popular NFT Markets** [[Paper](https://doi.org/10.1145/3589335.3651580)] `Measurement` · *NFT*
- (CIKM 2024) **Effective Illicit Account Detection on Large Cryptocurrency MultiGraphs** [[Paper](https://doi.org/10.1145/3627673.3679707)] [[Code](https://github.com/TommyDzh/DIAM)] `GNN` · *Crypto*

## On-chain Transaction & Graph Analytics

*Address clustering, account classification, de-anonymization and transaction graph learning.*

- (NeurIPS 2026) **RAMA: Resistance-Aware Multi-Hop Aggregation Graph Representation Learning for Robust Ethereum Account Classification** [[Paper](https://openreview.net/forum?id=E2j4hTCc0W)] `GNN` · *Ethereum*
- (WWW 2026) **TGweaver: Synthesizing Transaction Graphs for De-anonymization Analysis** [[Paper](https://doi.org/10.1145/3774904.3792318)] `Data-Synthesis` · *Mixer*
- (AAAI 2026) **IGT4ETH: An Isotropic Pre-trained Graph Transformer for Ethereum Account Classification** [[Paper](https://doi.org/10.1609/aaai.v40i28.39536)] [[Code](https://github.com/Camus-Code/IGT4ETH)] `GNN` `Pre-training` · *Ethereum*
- (NeurIPS 2025 D&B) **MiNT: Multi-Network Transfer Benchmark for Temporal Graph Learning** [[Paper](https://openreview.net/forum?id=Za7IcsXIRV)] [[Code](https://github.com/benjaminnNgo/ScalingTGNs)] `Temporal-Graph` `Transfer-Learning` · *Ethereum*
- (NeurIPS 2025 D&B) **The Temporal Graph of Bitcoin Transactions** [[Paper](https://openreview.net/forum?id=Xs7JM4VGHv)] [[Code](https://github.com/B1AAB/EBA)] `Temporal-Graph` · *Bitcoin*
- (KDD 2025) **Chainlet Orbits: Topological Address Embedding for Blockchain** [[Paper](https://doi.org/10.1145/3690624.3709322)] `Topological` · *Bitcoin*
- (WWW 2025) **Gamblers or Delegatees: Identifying Hidden Participant Roles in Crypto Casinos** [[Paper](https://doi.org/10.1145/3696410.3714689)] `Measurement` · *Crypto*
- (ICDM 2025) **When LLM Meets Simplicial Complex: A Novel Graph Prompt Learning on Ethereum Transaction Networks** [[Paper](https://doi.org/10.1109/icdm65498.2025.00148)] `LLM` `GNN` · *Ethereum*
- (ICDE 2025) **Know Your Account: Double Graph Inference-Based Account De-Anonymization on Ethereum** [[Paper](https://doi.org/10.1109/icde65448.2025.00102)] `GNN` · *Ethereum*
- (WSDM 2025) **Optimizing Blockchain Analysis: Tackling Temporality and Scalability with an Incremental Approach with Metropolis-Hastings Random Walks** [[Paper](https://doi.org/10.1145/3701551.3703521)] `Graph-Sampling` · *Crypto*
- (NeurIPS 2024 D&B) **Multi-Chain Graphs of Graphs: A New Approach to Analyzing Blockchain Datasets** [[Paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/3205b048f9cc54b9f7963db0b0f52d53-Abstract-Datasets_and_Benchmarks_Track.html)] [[Code](https://github.com/Xtra-Computing/Cryptocurrency-Graphs-of-graphs)] `GNN` · *Multi-chain*
- (ICLR 2024) **EX-Graph: A Pioneering Dataset Bridging Ethereum and X** [[Paper](https://openreview.net/forum?id=juE0rWGCJW)] `GNN` · *Ethereum*
- (KDD 2024) **BitLINK: Temporal Linkage of Address Clusters in Bitcoin Blockchain** [[Paper](https://doi.org/10.1145/3637528.3672037)] `Clustering` · *Bitcoin*
- (WWW 2024) **Exploring Unconfirmed Transactions for Effective Bitcoin Address Clustering** [[Paper](https://doi.org/10.1145/3589334.3645684)] `Clustering` · *Bitcoin*
- (WWW 2024 Companion) **Anonymity Analysis of the Umbra Stealth Address Scheme on Ethereum** [[Paper](https://doi.org/10.1145/3589335.3651963)] `Privacy` · *Ethereum*
- (WWW 2024 Companion) **Deanonymizing Transactions Originating from Monero Tor Hidden Service Nodes** [[Paper](https://doi.org/10.1145/3589335.3651487)] `Privacy` · *Monero*

## DeFi, MEV & Market Mechanisms

*AMMs and liquidity, MEV and block building, transaction fee mechanisms and token incentives.*

- (NeurIPS 2026) **Context Binding and Reusable Leakage in Threshold Decryption** [[Paper](https://openreview.net/forum?id=I8M8PZy2XG)] `Cryptography` `Encrypted-Mempool`
- (NeurIPS 2026) **Leakage Thresholds for Sandwich Equilibria Under Partial Information** [[Paper](https://openreview.net/forum?id=yuiJS0iLhX)] `Game-Theory` · *DEX*
- (WWW 2026) **Deterring A Small Collusion is All You Need** [[Paper](https://doi.org/10.1145/3774904.3792121)] `Mechanism-Design`
- (WWW 2026) **LiquidityPool: Game-Theoretic Analysis of Stakeholder Revenue in Ranking-Dependent DeFi** [[Paper](https://doi.org/10.1145/3774904.3792260)] `Game-Theory` · *DeFi*
- (WWW 2026 Companion) **Benchmarking Temporal Web3 Intelligence: Lessons from the FinSurvival 2025 Challenge** [[Paper](https://doi.org/10.1145/3774905.3795449)] `Survival-Analysis` · *DeFi*
- (ICDE 2026) **PRIME: Efficient Algorithm for Token Graph Routing Problem** [[Paper](https://doi.org/10.1109/icde65706.2026.00214)] `Graph-Algorithms` · *DEX*
- (WWW 2025) **Private Order Flows and Builder Bidding Dynamics: The Road to Monopoly in Ethereum's Block Building Market** [[Paper](https://doi.org/10.1145/3696410.3714754)] `Measurement` `Game-Theory` · *Ethereum*
- (IJCAI 2025) **Airdrop Games** [[Paper](https://doi.org/10.24963/ijcai.2025/431)] `Game-Theory` · *Token*
- (IJCAI 2025) **Smart Contracts for Trustless Sampling of Correlated Equilibria** [[Paper](https://doi.org/10.24963/ijcai.2025/416)] `Game-Theory` · *Ethereum*
- (KDD 2024) **Money Never Sleeps: Maximizing Liquidity Mining Yields in Decentralized Finance** [[Paper](https://doi.org/10.1145/3637528.3671942)] `Optimization` · *DeFi*
- (WWW 2024 Companion) **Measuring Arbitrage Losses and Profitability of AMM Liquidity** [[Paper](https://doi.org/10.1145/3589335.3651961)] `Measurement` · *DEX*

## NFT, DAO & Web3 Ecosystem

*NFT markets, DAO governance, memecoins, decentralized identity and naming services.*

- (KDD 2026) **DMind Benchmark: Toward a Holistic Assessment of LLM Capabilities across the Web3 Domain** [[Paper](https://doi.org/10.1145/3770855.3817512)] `LLM` · *Web3*
- (WWW 2026) **ShadowClone: Scalable Decentralized Identity with Cross-Domain Anonymity and Accountable Traceability** [[Paper](https://doi.org/10.1145/3774904.3792424)] `Cryptography` · *DID*
- (WWW 2026) **The Promise vs. Reality of NFT Decentralization: An Empirical Study of Storage Strategies and Defects** [[Paper](https://doi.org/10.1145/3774904.3792338)] `Measurement` · *NFT*
- (WWW 2026 Short) **Decentralized in Name Only: The Centralization of DAO Labor** [[Paper](https://hcmi.ee.torontomu.ca/publication/decentralized-in-name-only-centralization-dao-labor/)] `Qualitative` · *DAO*
- (KDD 2025) **Breeding-aware Revenue Maximization for NFT Viral Marketing on Social Networks** [[Paper](https://doi.org/10.1145/3711896.3736867)] `Influence-Maximization` · *NFT*
- (WWW 2025) **Beyond Visual Confusion: Understanding How Inconsistencies in ENS Normalization Facilitate Homoglyph Attacks** [[Paper](https://doi.org/10.1145/3696410.3714675)] `Measurement` · *ENS*
- (WWW 2025) **Fully Anonymous Decentralized Identity Supporting Threshold Traceability with Practical Blockchain** [[Paper](https://doi.org/10.1145/3696410.3714762)] `Cryptography` · *DID*
- (WWW 2025) **Linking Souls to Humans: Blockchain Accounts with Credible Anonymity for Web 3.0 Decentralized Identity** [[Paper](https://doi.org/10.1145/3696410.3714784)] `Cryptography` · *DID*
- (WWW 2025) **NFTs as a Data-Rich Test Bed: Conspicuous Consumption and its Determinants** [[Paper](https://doi.org/10.1145/3696410.3714724)] `Economics` · *NFT*
- (WWW 2025 Companion) **Bridging Culture and Finance: A Multimodal Analysis of Memecoins in the Web3 Ecosystem** [[Paper](https://doi.org/10.1145/3701716.3715561)] [[Code](https://github.com/hwlongCUHK/Coin-Meme)] `Multimodal` · *Memecoin*
- (CIKM 2025) **CoinCLIP: A Multimodal Framework for Assessing Viability in Web3 Memecoins** [[Paper](https://doi.org/10.1145/3746252.3760881)] `Multimodal` · *Memecoin*
- (ICDM 2025) **Equilibrium-Based NFT Marketplace Recommendation for NFTs with Breeding** [[Paper](https://doi.org/10.1109/icdm65498.2025.00094)] [[Code](https://github.com/jimmy-academia/BANTER)] `Recommendation` `Game-Theory` · *NFT*
- (WWW 2024) **IDEA-DAC: Integrity-Driven Editing for Accountable Decentralized Anonymous Credentials via ZK-JSON** [[Paper](https://doi.org/10.1145/3589334.3645658)] [[Code](https://github.com/Nullus-Labs/IDEA-DAC)] `Cryptography` · *DID*
- (WWW 2024) **Investigations of Top-Level Domain Name Collisions in Blockchain Naming Services** [[Paper](https://doi.org/10.1145/3589334.3645459)] `Measurement` · *ENS*
- (WWW 2024) **Unveiling the Paradox of NFT Prosperity** [[Paper](https://doi.org/10.1145/3589334.3645566)] `Measurement` · *NFT*
- (WWW 2024 Companion) **Characterizing the Solana NFT Ecosystem** [[Paper](https://doi.org/10.1145/3589335.3651478)] `Measurement` · *Solana, NFT*
- (WWW 2024 Companion) **Concentration of Power and Participation in Online Governance: the Ecosystem of Decentralized Autonomous Organizations** [[Paper](https://doi.org/10.1145/3589335.3651481)] `Measurement` · *DAO*

## Smart Contract Security & Analysis

*Vulnerability detection, program analysis, decompilation, code generation and auditing agents.*

- (NeurIPS 2026) **Reinforcement Learning-Guided Symbolic Execution for Efficient and Exploitable Smart Contract Analysis** [[Paper](https://openreview.net/forum?id=0NgpgjG8bV)] `RL` `Symbolic-Execution` · *Ethereum*
- (ICML 2026) **EVMbench: Evaluating AI Agents on Smart Contract Security** [[Paper](https://openreview.net/forum?id=K5S8N5NgD8)] [[Code](https://github.com/paradigmxyz/evmbench)] `LLM` `Agent` · *Ethereum*
- (AAAI 2026) **BugSweeper: Function-Level Detection of Smart Contract Vulnerabilities Using Graph Neural Networks** [[Paper](https://doi.org/10.1609/aaai.v40i1.37021)] `GNN` · *Ethereum*
- (ACL 2026) **EVM-QuestBench: An Execution-Grounded Benchmark for Natural-Language Transaction Code Generation** [[Paper](https://doi.org/10.18653/v1/2026.acl-long.1642)] [[Code](https://github.com/OpenEdgeHQ/EVM-quest-bench)] `LLM` · *Ethereum*
- (ACL 2026) **Towards Trustworthy Smart Contract Synthesis: A Multi-Agent Framework with Lean-Based Verification** [[Paper](https://doi.org/10.18653/v1/2026.acl-long.1836)] `LLM` `Agent` `Formal-Verification` · *Ethereum*
- (WWW 2025) **Quantitative Runtime Monitoring of Ethereum Transaction Attacks** [[Paper](https://doi.org/10.1145/3696410.3714682)] `Runtime-Verification` · *Ethereum*
- (WWW 2025) **SigScope: Detecting and Understanding Off-Chain Message Signing-related Vulnerabilities in Decentralized Applications** [[Paper](https://doi.org/10.1145/3696410.3714686)] `Program-Analysis` · *DApp*
- (WWW 2025) **SuiGPT MAD: Move AI Decompiler to Improve Transparency and Auditability on Non-Open-Source Blockchain Smart Contract** [[Paper](https://doi.org/10.1145/3696410.3714790)] `LLM` · *Sui*
- (AAAI 2025) **CLEP: A Novel Contrastive Learning Method for Evolutionary Reentrancy Vulnerability Detection** [[Paper](https://doi.org/10.1609/aaai.v39i1.31981)] `Contrastive` · *Ethereum*
- (AAAI 2025) **MTVHunter: Smart Contracts Vulnerability Detection Based on Multi-Teacher Knowledge Translation** [[Paper](https://doi.org/10.1609/aaai.v39i14.33664)] [[Code](https://github.com/KD-SCVD/MTVHunter)] `Knowledge-Distillation` · *Ethereum*
- (AAAI 2025) **SCALM: Detecting Bad Practices in Smart Contracts Through LLMs** [[Paper](https://doi.org/10.1609/aaai.v39i1.32026)] `LLM` · *Ethereum*
- (IJCAI 2025) **Guiding LLM-based Smart Contract Generation with Finite State Machine** [[Paper](https://doi.org/10.24963/ijcai.2025/653)] `LLM` · *Ethereum*
- (EMNLP 2025) **SolEval: Benchmarking Large Language Models for Repository-level Solidity Smart Contract Generation** [[Paper](https://doi.org/10.18653/v1/2025.emnlp-main.218)] [[Code](https://github.com/pzy2000/SolEval)] `LLM` · *Ethereum*
- (NeurIPS 2024) **Detecting Bugs with Substantial Monetary Consequences by LLM and Rule-based Reasoning** [[Paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/f1d8400fec75f683c4d823f5836a81bb-Abstract-Conference.html)] `LLM` `Program-Analysis` · *Ethereum*
- (WWW 2024) **Characterizing Ethereum Upgradable Smart Contracts and Their Security Implications** [[Paper](https://doi.org/10.1145/3589334.3645640)] `Measurement` · *Ethereum*
- (WWW 2024 Companion) **DeFiTail: DeFi Protocol Inspection through Cross-Contract Execution Analysis** [[Paper](https://doi.org/10.1145/3589335.3651488)] `Program-Analysis` · *DeFi*
- (WWW 2024 Companion) **StateGuard: Detecting State Derailment Defects in Decentralized Exchange Smart Contract** [[Paper](https://doi.org/10.1145/3589335.3651562)] `Program-Analysis` · *DEX*
- (IJCAI 2024) **EFEVD: Enhanced Feature Extraction for Smart Contract Vulnerability Detection** [[Paper](https://doi.org/10.24963/ijcai.2024/469)] `Deep-Learning` `Vulnerability-Detection` · *Ethereum*
- (ICDE 2024) **MuFuzz: Sequence-Aware Mutation and Seed Mask Guidance for Blockchain Smart Contract Fuzzing** [[Paper](https://doi.org/10.1109/icde60146.2024.00158)] [[Code](https://github.com/OMH4ck/mufuzz)] `Fuzzing` · *Ethereum*

## Blockchain Systems & Infrastructure

*Sharding, consensus, transaction execution, storage and query processing, P2P and cross-chain security.*

- (WWW 2026) **Alzo: Auto-Tuning with Reinforcement Learning for DAG-based Blockchains** [[Paper](https://doi.org/10.1145/3774904.3792448)] `RL` · *DAG*
- (WWW 2026) **BIND: Enabling Continuous Transaction Processing During Account Migration in Sharded Blockchains** [[Paper](https://doi.org/10.1145/3774904.3792530)] `Sharding`
- (WWW 2026) **Concordia: Enabling Low-Conflict Distributed Transaction Scheduling in Sharding Blockchain via Cooperative Perception** [[Paper](https://doi.org/10.1145/3774904.3792469)] `Sharding`
- (WWW 2026) **Eclipse Attacks on Ethereum's Peer-to-Peer Network** [[Paper](https://doi.org/10.1145/3774904.3792231)] `P2P-Security` · *Ethereum*
- (WWW 2026) **Greedy Attack: Breaking Finality against VeChain Proof-of-Authority Consensus Protocol** [[Paper](https://doi.org/10.1145/3774904.3792513)] `Consensus-Security` · *VeChain*
- (WWW 2026) **On the Effectiveness of Mempool-based Transaction Auditing** [[Paper](https://doi.org/10.1145/3774904.3792404)] `Measurement` · *Ethereum*
- (WWW 2026) **Risk-free Selfish Mining in Hybrid Predictability Model. A Case Study on Polkadot's NPoS** [[Paper](https://doi.org/10.1145/3774904.3792560)] `Game-Theory` · *Polkadot*
- (WWW 2026 Companion) **A Taxonomy-Driven Cryptographic Dependency Inventory for Post-Quantum Migration in Decentralized Systems: Triage Rules and a Worked Example** [[Paper](https://doi.org/10.1145/3774905.3794696)] `Post-Quantum`
- (ICDE 2026) **Banknote-Chain: Achieving User-Incentivized Parallelism in Blockchain via a Banknote-Inspired Transaction Model** [[Paper](https://doi.org/10.1109/icde65706.2026.00055)] [[Code](https://github.com/zhiyongm/Banknote-Chain)] `Systems`
- (ICDE 2026) **Chubby: Robust Smart Contract Execution Against Dependency Over-Declaration** [[Paper](https://doi.org/10.1109/icde65706.2026.00119)] `Concurrency`
- (ICDE 2026) **Cole⁺: Towards Practical Column-Based Learned Storage for Blockchain Systems** [[Paper](https://doi.org/10.1109/icde65706.2026.00132)] `Learned-Index` `Storage`
- (ICDE 2026) **GECO: A Confidentiality-Preserving and High-Performance Permissioned Blockchain Framework for General Smart Contracts** [[Paper](https://doi.org/10.1109/icde65706.2026.00155)] `Systems` · *Permissioned*
- (ICDE 2026) **Rethinking BFT Consensus via Transaction-Level Protocol Construction for Optimal Performance** [[Paper](https://doi.org/10.1109/icde65706.2026.00361)] `Consensus`
- (ICDE 2026) **RoarChain: A Robust Sharding Blockchain System for Enterprise Consortium** [[Paper](https://doi.org/10.1109/icde65706.2026.00014)] `Sharding` · *Permissioned*
- (ICDE 2026) **SpendableStore: A UTXO-Based Decentralized Data Store** [[Paper](https://doi.org/10.1109/icde65706.2026.00153)] `Storage` · *UTXO*
- (WWW 2025) **AERO: Enhancing Sharding Blockchain via Deep Reinforcement Learning for Account Migration** [[Paper](https://doi.org/10.1145/3696410.3714926)] `RL` `Sharding`
- (WWW 2025) **MAP the Blockchain World: A Trustless and Scalable Blockchain Interoperability Protocol for Cross-chain Applications** [[Paper](https://doi.org/10.1145/3696410.3714867)] `Interoperability` · *Multi-chain*
- (ICDE 2025) **E³FS: Efficient, Secure, and Verifiable Fuzzy Search with Data Updates in Hybrid-Storage Blockchains** [[Paper](https://doi.org/10.1109/icde65448.2025.00290)] `Query-Processing`
- (ICDE 2025) **Loom: A Deterministic Execution Framework Towards Nested Contract Transactions** [[Paper](https://doi.org/10.1109/icde65448.2025.00182)] `Concurrency` · *Permissioned*
- (ICDE 2025) **MEST: An Efficient Authenticated Secondary Index in Blockchain Systems** [[Paper](https://doi.org/10.1109/icde65448.2025.00126)] `Indexing`
- (ICDE 2025) **Towards Dynamic Boolean Range Query Over Hybrid-Storage Blockchains: A Secure and Reliably Verifiable Framework** [[Paper](https://doi.org/10.1109/icde65448.2025.00128)] `Query-Processing`
- (ICDE 2025) **VGQ: Enabling Verifiable Graph Queries on Blockchain Systems** [[Paper](https://doi.org/10.1109/icde65448.2025.00269)] `Query-Processing`
- (WWW 2024) **Advancing Web 3.0: Making Smart Contracts Smarter on Blockchain** [[Paper](https://doi.org/10.1145/3589334.3645319)] `AI-Inference` `Systems` · *Ethereum*
- (WWW 2024) **Blockchain Censorship** [[Paper](https://doi.org/10.1145/3589334.3645431)] `Measurement` · *Ethereum*
- (WWW 2024) **SPRING: Improving the Throughput of Sharding Blockchain via Deep Reinforcement Learning Based State Placement** [[Paper](https://doi.org/10.1145/3589334.3645386)] `RL` `Sharding`
- (WWW 2024 Companion) **Distributed Transparent Data Layer for Next Generation Blockchains** [[Paper](https://doi.org/10.1145/3589335.3651255)] `Systems`
- (WWW 2024 Companion) **Seamlessly Transferring Assets through Layer-0 Bridges: An Empirical Analysis of Stargate Bridge's Architecture and Dynamics** [[Paper](https://doi.org/10.1145/3589335.3651964)] `Measurement` · *Cross-chain*
- (WWW 2024 Companion) **Statistical Confidence in Mining Power Estimates for PoW Blockchains** [[Paper](https://doi.org/10.1145/3589335.3651960)] `Statistics` · *PoW*
- (AAAI 2024) **Approval-Based Committee Voting in Practice: A Case Study of (over-)Representation in the Polkadot Blockchain** [[Paper](https://doi.org/10.1609/aaai.v38i9.28807)] `Social-Choice` · *Polkadot*
- (CIKM 2024) **HTFabric: A Fast Re-ordering and Parallel Re-execution Method for a High-Throughput Blockchain** [[Paper](https://doi.org/10.1145/3627673.3679606)] [[Code](https://github.com/jaeyubsong/HTFabric)] `Systems` · *Permissioned*
- (ICDE 2024) **Authenticated Keyword Search on Large-Scale Graphs in Hybrid-Storage Blockchains** [[Paper](https://doi.org/10.1109/icde60146.2024.00155)] `Query-Processing`
- (ICDE 2024) **Authenticated Subgraph Matching in Hybrid-Storage Blockchains** [[Paper](https://doi.org/10.1109/icde60146.2024.00159)] `Query-Processing`
- (ICDE 2024) **Efficient Partial Order Based Transaction Processing for Permissioned Blockchains** [[Paper](https://doi.org/10.1109/icde60146.2024.00152)] `Systems` · *Permissioned*
- (ICDE 2024) **Enabling Efficient, Verifiable, and Secure Conjunctive Keyword Search in Hybrid-Storage Blockchains** [[Paper](https://doi.org/10.1109/icde60146.2024.00481)] `Query-Processing`
- (ICDE 2024) **Porygon: Scaling Blockchain via 3D Parallelism** [[Paper](https://doi.org/10.1109/icde60146.2024.00153)] `Systems`
- (ICDE 2024) **SharDAG: Scaling DAG-Based Blockchains Via Adaptive Sharding** [[Paper](https://doi.org/10.1109/icde60146.2024.00165)] `Sharding`
- (ICDE 2024) **SpotLess: Concurrent Rotational Consensus Made Practical Through Rapid View Synchronization** [[Paper](https://doi.org/10.1109/icde60146.2024.00157)] `Consensus`
- (ICDE 2024) **TELL: Efficient Transaction Execution Protocol Towards Leaderless Consensus** [[Paper](https://doi.org/10.1109/icde60146.2024.00154)] `Consensus` · *Permissioned*
- (ICDE 2024) **V2FS : A Verifiable Virtual Filesystem for Multi-Chain Query Authentication** [[Paper](https://doi.org/10.1109/icde60146.2024.00160)] `Query-Processing` · *Multi-chain*

## Surveys, Tutorials & Workshops

*Surveys, tutorials and workshop summaries held at the covered conferences.*

- (WWW 2026 Companion) **Quantum-Safe, Efficient, and AI-Enhanced Blockchains for the Web: A Cooperative Tutorial on Quantum Computing, Blockchain Applications, and Data Standards** [[Paper](https://doi.org/10.1145/3774905.3793916)] `Tutorial`
- (WWW 2026 Companion) **ZABAPAD 2026: 1st Workshop on Zero-knowledge Proof and Blockchain for WEB 4.0: Advancing the Post-quantum and Decentralized Era** [[Paper](https://doi.org/10.1145/3774905.3794693)] `Workshop`
- (IJCAI 2026) **Large Language Models for Blockchain Security and Analytics: A Survey** [[Paper](https://doi.org/10.24963/ijcai.2026/885)] `LLM` `Survey`
- (KDD 2024) **The Fourth International Workshop on Smart Data for Blockchain and Distributed Ledger (SDBD'24)** [[Paper](https://doi.org/10.1145/3637528.3671475)] `Workshop`
- (WWW 2024 Companion) **CAAW'24: The 3rd International Cryptoasset Analytics Workshop** [[Paper](https://doi.org/10.1145/3589335.3641304)] `Workshop`
- (WWW 2024 Companion) **Incentives in the Ether: Practical Cryptocurrency Economics & Security** [[Paper](https://doi.org/10.1145/3589335.3651268)] `Tutorial`
- (WWW 2024 Companion) **When Crypto Economics Meet Graph Analytics and Learning** [[Paper](https://doi.org/10.1145/3589335.3651257)] `Tutorial`
- (IJCAI 2024) **Survey on Strategic Mining in Blockchain: A Reinforcement Learning Approach** [[Paper](https://doi.org/10.24963/ijcai.2024/1170)] `RL` `Survey`

# Papers by Year

[Back to top](#table-of-contents)

## 2026

- (NeurIPS 2026) **Context Binding and Reusable Leakage in Threshold Decryption** [[Paper](https://openreview.net/forum?id=I8M8PZy2XG)] `Cryptography` `Encrypted-Mempool` — *DeFi, MEV & Market Mechanisms*
- (NeurIPS 2026) **Generating Financial Time Series by Matching Random Convolutional Features** ＊ [[Paper](https://openreview.net/forum?id=tLVW1Y9hBz)] `Generative` `Time-Series` · *Crypto* — *Price Forecasting & Market Analysis*
- (NeurIPS 2026) **Leakage Thresholds for Sandwich Equilibria Under Partial Information** [[Paper](https://openreview.net/forum?id=yuiJS0iLhX)] `Game-Theory` · *DEX* — *DeFi, MEV & Market Mechanisms*
- (NeurIPS 2026) **Market Regime Council for Dynamic Credit Assignment in Multi-Agent LLM Decision Systems** [[Paper](https://openreview.net/forum?id=xuhyMmn0D0)] `LLM` `Agent` · *Crypto* — *Trading & Portfolio Management*
- (NeurIPS 2026) **RAMA: Resistance-Aware Multi-Hop Aggregation Graph Representation Learning for Robust Ethereum Account Classification** [[Paper](https://openreview.net/forum?id=E2j4hTCc0W)] `GNN` · *Ethereum* — *On-chain Transaction & Graph Analytics*
- (NeurIPS 2026) **Reinforcement Learning-Guided Symbolic Execution for Efficient and Exploitable Smart Contract Analysis** [[Paper](https://openreview.net/forum?id=0NgpgjG8bV)] `RL` `Symbolic-Execution` · *Ethereum* — *Smart Contract Security & Analysis*
- (ICML 2026) **EVMbench: Evaluating AI Agents on Smart Contract Security** [[Paper](https://openreview.net/forum?id=K5S8N5NgD8)] [[Code](https://github.com/paradigmxyz/evmbench)] `LLM` `Agent` · *Ethereum* — *Smart Contract Security & Analysis*
- (ICML 2026) **Scam2Prompt: A Scalable Framework for Auditing Malicious Scam Endpoints in Production LLMs** ＊ [[Paper](https://openreview.net/forum?id=jEQQBE30m1)] [[Code](https://github.com/Scam2Prompt/Scam2Prompt)] `LLM` · *Web3* — *Fraud, Scam & Attack Detection*
- (ICLR 2026) **CTBench: Cryptocurrency Time Series Generation Benchmark** [[Paper](https://openreview.net/forum?id=RzT2sombPD)] `Generative` `Time-Series` · *Crypto* — *Price Forecasting & Market Analysis*
- (ICLR 2026) **Trade in Minutes! Rationality-Driven Agentic System for Quantitative Financial Trading** ＊ [[Paper](https://openreview.net/forum?id=ROEwZAxqyS)] `LLM` `Agent` · *Crypto* — *Trading & Portfolio Management*
- (ICLR 2026 Workshop) **Probabilistic Multivariate Time Series Forecasting with Diffusion Copulas** [[Paper](https://arxiv.org/abs/2605.19685)] `Diffusion` `Time-Series` · *Crypto* — *Price Forecasting & Market Analysis*
- (KDD 2026) **DMind Benchmark: Toward a Holistic Assessment of LLM Capabilities across the Web3 Domain** [[Paper](https://doi.org/10.1145/3770855.3817512)] `LLM` · *Web3* — *NFT, DAO & Web3 Ecosystem*
- (KDD 2026) **FineFT: Efficient and Risk-Aware Ensemble Reinforcement Learning for Futures Trading** [[Paper](https://doi.org/10.1145/3770854.3780187)] `RL` · *Crypto* — *Trading & Portfolio Management*
- (KDD 2026) **Towards Event-Aware Forecasting in DeFi: Insights from On-chain Automated Market Maker Protocols** [[Paper](https://doi.org/10.1145/3770855.3817502)] [[Code](https://github.com/finbrain-lab-hkustgz/Deep-AMM-Events)] `Time-Series` · *DEX* — *Price Forecasting & Market Analysis*
- (WWW 2026) **Alzo: Auto-Tuning with Reinforcement Learning for DAG-based Blockchains** [[Paper](https://doi.org/10.1145/3774904.3792448)] `RL` · *DAG* — *Blockchain Systems & Infrastructure*
- (WWW 2026) **Analysis of CEX-DEX Arbitrage Opportunities with Hidden Markov Models** [[Paper](https://doi.org/10.1145/3774904.3792185)] `HMM` · *DEX* — *Trading & Portfolio Management*
- (WWW 2026) **BIND: Enabling Continuous Transaction Processing During Account Migration in Sharded Blockchains** [[Paper](https://doi.org/10.1145/3774904.3792530)] `Sharding` — *Blockchain Systems & Infrastructure*
- (WWW 2026) **Concordia: Enabling Low-Conflict Distributed Transaction Scheduling in Sharding Blockchain via Cooperative Perception** [[Paper](https://doi.org/10.1145/3774904.3792469)] `Sharding` — *Blockchain Systems & Infrastructure*
- (WWW 2026) **Deterring A Small Collusion is All You Need** [[Paper](https://doi.org/10.1145/3774904.3792121)] `Mechanism-Design` — *DeFi, MEV & Market Mechanisms*
- (WWW 2026) **Eclipse Attacks on Ethereum's Peer-to-Peer Network** [[Paper](https://doi.org/10.1145/3774904.3792231)] `P2P-Security` · *Ethereum* — *Blockchain Systems & Infrastructure*
- (WWW 2026) **Evasion Under Blockchain Sanctions** [[Paper](https://doi.org/10.1145/3774904.3792715)] `Measurement` · *Ethereum* — *Fraud, Scam & Attack Detection*
- (WWW 2026) **Greedy Attack: Breaking Finality against VeChain Proof-of-Authority Consensus Protocol** [[Paper](https://doi.org/10.1145/3774904.3792513)] `Consensus-Security` · *VeChain* — *Blockchain Systems & Infrastructure*
- (WWW 2026) **LiquidityPool: Game-Theoretic Analysis of Stakeholder Revenue in Ranking-Dependent DeFi** [[Paper](https://doi.org/10.1145/3774904.3792260)] `Game-Theory` · *DeFi* — *DeFi, MEV & Market Mechanisms*
- (WWW 2026) **Multi-Modal Enhanced Graph Transfer Learning for Digital Finance Fraud Detection** [[Paper](https://doi.org/10.1145/3774904.3792946)] `GNN` `Multimodal` `Transfer-Learning` · *Crypto* — *Fraud, Scam & Attack Detection*
- (WWW 2026) **On the Effectiveness of Mempool-based Transaction Auditing** [[Paper](https://doi.org/10.1145/3774904.3792404)] `Measurement` · *Ethereum* — *Blockchain Systems & Infrastructure*
- (WWW 2026) **Resisting Manipulative Bots in Meme Coin Copy Trading: A Multi-Agent Approach with Chain-of-Thought Reasoning** [[Paper](https://arxiv.org/abs/2601.08641)] `LLM` `Multi-Agent` · *Memecoin* — *Trading & Portfolio Management*
- (WWW 2026) **Risk-free Selfish Mining in Hybrid Predictability Model. A Case Study on Polkadot's NPoS** [[Paper](https://doi.org/10.1145/3774904.3792560)] `Game-Theory` · *Polkadot* — *Blockchain Systems & Infrastructure*
- (WWW 2026) **ShadowClone: Scalable Decentralized Identity with Cross-Domain Anonymity and Accountable Traceability** [[Paper](https://doi.org/10.1145/3774904.3792424)] `Cryptography` · *DID* — *NFT, DAO & Web3 Ecosystem*
- (WWW 2026) **TGweaver: Synthesizing Transaction Graphs for De-anonymization Analysis** [[Paper](https://doi.org/10.1145/3774904.3792318)] `Data-Synthesis` · *Mixer* — *On-chain Transaction & Graph Analytics*
- (WWW 2026) **The Promise vs. Reality of NFT Decentralization: An Empirical Study of Storage Strategies and Defects** [[Paper](https://doi.org/10.1145/3774904.3792338)] `Measurement` · *NFT* — *NFT, DAO & Web3 Ecosystem*
- (WWW 2026) **Understanding Post-Exploit Laundering Behavior on Ethereum** [[Paper](https://doi.org/10.1145/3774904.3792918)] `Measurement` · *Ethereum* — *Fraud, Scam & Attack Detection*
- (WWW 2026 Companion) **A Taxonomy-Driven Cryptographic Dependency Inventory for Post-Quantum Migration in Decentralized Systems: Triage Rules and a Worked Example** [[Paper](https://doi.org/10.1145/3774905.3794696)] `Post-Quantum` — *Blockchain Systems & Infrastructure*
- (WWW 2026 Companion) **Benchmarking Temporal Web3 Intelligence: Lessons from the FinSurvival 2025 Challenge** [[Paper](https://doi.org/10.1145/3774905.3795449)] `Survival-Analysis` · *DeFi* — *DeFi, MEV & Market Mechanisms*
- (WWW 2026 Short) **Decentralized in Name Only: The Centralization of DAO Labor** [[Paper](https://hcmi.ee.torontomu.ca/publication/decentralized-in-name-only-centralization-dao-labor/)] `Qualitative` · *DAO* — *NFT, DAO & Web3 Ecosystem*
- (WWW 2026 Companion) **Learning-Based Optimization of Atomic Arbitrage in Decentralized Financial Systems** [[Paper](https://doi.org/10.1145/3774905.3794707)] `Optimization` · *DEX* — *Trading & Portfolio Management*
- (WWW 2026 Companion) **Quantum-Safe, Efficient, and AI-Enhanced Blockchains for the Web: A Cooperative Tutorial on Quantum Computing, Blockchain Applications, and Data Standards** [[Paper](https://doi.org/10.1145/3774905.3793916)] `Tutorial` — *Surveys, Tutorials & Workshops*
- (WWW 2026 Companion) **ZABAPAD 2026: 1st Workshop on Zero-knowledge Proof and Blockchain for WEB 4.0: Advancing the Post-quantum and Decentralized Era** [[Paper](https://doi.org/10.1145/3774905.3794693)] `Workshop` — *Surveys, Tutorials & Workshops*
- (AAAI 2026) **ArchetypeTrader: Reinforcement Learning for Selecting and Refining Learnable Strategic Archetypes in Quantitative Trading** [[Paper](https://doi.org/10.1609/aaai.v40i34.40166)] [[Code](https://github.com/yfcck/ArchetypeTrader)] `RL` · *Crypto* — *Trading & Portfolio Management*
- (AAAI 2026) **BugSweeper: Function-Level Detection of Smart Contract Vulnerabilities Using Graph Neural Networks** [[Paper](https://doi.org/10.1609/aaai.v40i1.37021)] `GNN` · *Ethereum* — *Smart Contract Security & Analysis*
- (AAAI 2026) **IGT4ETH: An Isotropic Pre-trained Graph Transformer for Ethereum Account Classification** [[Paper](https://doi.org/10.1609/aaai.v40i28.39536)] [[Code](https://github.com/Camus-Code/IGT4ETH)] `GNN` `Pre-training` · *Ethereum* — *On-chain Transaction & Graph Analytics*
- (AAAI 2026) **Market-Aware Event Timeline Summarization: Integrating Price Signals to Improve Financial News Understanding** [[Paper](https://doi.org/10.1609/aaai.v40i48.42370)] `LLM` `NLP` · *Crypto* — *Price Forecasting & Market Analysis*
- (IJCAI 2026) **Large Language Models for Blockchain Security and Analytics: A Survey** [[Paper](https://doi.org/10.24963/ijcai.2026/885)] `LLM` `Survey` — *Surveys, Tutorials & Workshops*
- (IJCAI 2026) **Temporal Motif-aware Graph Test-time Adaptation for OOD Blockchain Anomaly Detection** [[Paper](https://doi.org/10.24963/ijcai.2026/802)] [[Code](https://github.com/LuoXishuang0712/TEMG-TTA)] `GNN` `Temporal-Graph` · *Crypto* — *Fraud, Scam & Attack Detection*
- (ICDE 2026) **Banknote-Chain: Achieving User-Incentivized Parallelism in Blockchain via a Banknote-Inspired Transaction Model** [[Paper](https://doi.org/10.1109/icde65706.2026.00055)] [[Code](https://github.com/zhiyongm/Banknote-Chain)] `Systems` — *Blockchain Systems & Infrastructure*
- (ICDE 2026) **Chubby: Robust Smart Contract Execution Against Dependency Over-Declaration** [[Paper](https://doi.org/10.1109/icde65706.2026.00119)] `Concurrency` — *Blockchain Systems & Infrastructure*
- (ICDE 2026) **Cole⁺: Towards Practical Column-Based Learned Storage for Blockchain Systems** [[Paper](https://doi.org/10.1109/icde65706.2026.00132)] `Learned-Index` `Storage` — *Blockchain Systems & Infrastructure*
- (ICDE 2026) **GECO: A Confidentiality-Preserving and High-Performance Permissioned Blockchain Framework for General Smart Contracts** [[Paper](https://doi.org/10.1109/icde65706.2026.00155)] `Systems` · *Permissioned* — *Blockchain Systems & Infrastructure*
- (ICDE 2026) **PRIME: Efficient Algorithm for Token Graph Routing Problem** [[Paper](https://doi.org/10.1109/icde65706.2026.00214)] `Graph-Algorithms` · *DEX* — *DeFi, MEV & Market Mechanisms*
- (ICDE 2026) **Rethinking BFT Consensus via Transaction-Level Protocol Construction for Optimal Performance** [[Paper](https://doi.org/10.1109/icde65706.2026.00361)] `Consensus` — *Blockchain Systems & Infrastructure*
- (ICDE 2026) **RoarChain: A Robust Sharding Blockchain System for Enterprise Consortium** [[Paper](https://doi.org/10.1109/icde65706.2026.00014)] `Sharding` · *Permissioned* — *Blockchain Systems & Infrastructure*
- (ICDE 2026) **SpendableStore: A UTXO-Based Decentralized Data Store** [[Paper](https://doi.org/10.1109/icde65706.2026.00153)] `Storage` · *UTXO* — *Blockchain Systems & Infrastructure*
- (ICDE 2026) **TRADER: Real-time Arbitrage Detection via Negative Cycles on Dynamic Graphs** [[Paper](https://doi.org/10.1109/icde65706.2026.00141)] `Graph-Algorithms` · *DEX* — *Trading & Portfolio Management*
- (SIGIR 2026) **TDHGNN: A Temporal Directed Hypergraph Neural Network for Bitcoin Fraud Detection** [[Paper](https://doi.org/10.1145/3805712.3809899)] [[Code](https://github.com/KellyGong/TDHGNN)] `Hypergraph` `Temporal-Graph` · *Bitcoin* — *Fraud, Scam & Attack Detection*
- (ACL 2026) **EVM-QuestBench: An Execution-Grounded Benchmark for Natural-Language Transaction Code Generation** [[Paper](https://doi.org/10.18653/v1/2026.acl-long.1642)] [[Code](https://github.com/OpenEdgeHQ/EVM-quest-bench)] `LLM` · *Ethereum* — *Smart Contract Security & Analysis*
- (ACL 2026) **Towards Trustworthy Smart Contract Synthesis: A Multi-Agent Framework with Lean-Based Verification** [[Paper](https://doi.org/10.18653/v1/2026.acl-long.1836)] `LLM` `Agent` `Formal-Verification` · *Ethereum* — *Smart Contract Security & Analysis*

## 2025

- (NeurIPS 2025) **BlockScan: Detecting Anomalies in Blockchain Transactions** [[Paper](https://openreview.net/forum?id=URB690A5r5)] `Transformer` `LLM` · *Crypto* — *Fraud, Scam & Attack Detection*
- (NeurIPS 2025) **OPHR: Mastering Volatility Trading with Multi-Agent Deep Reinforcement Learning** [[Paper](https://openreview.net/forum?id=2p4AtivyZz)] [[Code](https://github.com/Edwicn/OPHR-MasteringVolatilityTradingwithMultiAgentDeepReinforcementLearning)] `RL` `Multi-Agent` · *Bitcoin, Ethereum* — *Trading & Portfolio Management*
- (NeurIPS 2025 D&B) **MiNT: Multi-Network Transfer Benchmark for Temporal Graph Learning** [[Paper](https://openreview.net/forum?id=Za7IcsXIRV)] [[Code](https://github.com/benjaminnNgo/ScalingTGNs)] `Temporal-Graph` `Transfer-Learning` · *Ethereum* — *On-chain Transaction & Graph Analytics*
- (NeurIPS 2025 Workshop) **Orchestration Framework for Financial Agents: From Algorithmic Trading to Agentic Trading** ＊ [[Paper](https://arxiv.org/abs/2512.02227)] [[Code](https://github.com/Open-Finance-Lab/AgenticTrading)] `LLM` `Agent` · *Crypto* — *Trading & Portfolio Management*
- (NeurIPS 2025 D&B) **The Temporal Graph of Bitcoin Transactions** [[Paper](https://openreview.net/forum?id=Xs7JM4VGHv)] [[Code](https://github.com/B1AAB/EBA)] `Temporal-Graph` · *Bitcoin* — *On-chain Transaction & Graph Analytics*
- (ICML 2025) **Pareto-Optimality, Smoothness, and Stochasticity in Learning-Augmented One-Max-Search** ＊ [[Paper](https://openreview.net/forum?id=ZTOVlPC5Vf)] `Online-Algorithms` · *Bitcoin* — *Trading & Portfolio Management*
- (ICLR 2025 Workshop) **Exploring LLM Cryptocurrency Trading Through Fact-Subjectivity Aware Reasoning** [[Paper](https://arxiv.org/abs/2410.12464)] [[Code](https://github.com/HaeSe0ng/FS-ReasoningAgent)] `LLM` · *Crypto* — *Trading & Portfolio Management*
- (ICLR 2025 Workshop) **FinTSBridge: A New Evaluation Suite for Real-world Financial Prediction with Advanced Time Series Models** ＊ [[Paper](https://arxiv.org/abs/2503.06928)] `Time-Series` · *Crypto* — *Price Forecasting & Market Analysis*
- (KDD 2025) **Breeding-aware Revenue Maximization for NFT Viral Marketing on Social Networks** [[Paper](https://doi.org/10.1145/3711896.3736867)] `Influence-Maximization` · *NFT* — *NFT, DAO & Web3 Ecosystem*
- (KDD 2025) **Chainlet Orbits: Topological Address Embedding for Blockchain** [[Paper](https://doi.org/10.1145/3690624.3709322)] `Topological` · *Bitcoin* — *On-chain Transaction & Graph Analytics*
- (KDD 2025) **CryptoMixer: Fine-grained market information-aware MLP Networks for Individual Cryptocurrency Trading Prediction** [[Paper](https://doi.org/10.1145/3711896.3736900)] [[Code](https://github.com/aqua111000/CryptoMixer)] `MLP` `Time-Series` · *Crypto* — *Price Forecasting & Market Analysis*
- (KDD 2025) **TEMPER: Capturing Consistent and Fluctuating TEMPoral User Behaviour for EtheReum Phishing Scam Detection** [[Paper](https://doi.org/10.1145/3690624.3709399)] `Temporal-Graph` · *Ethereum* — *Fraud, Scam & Attack Detection*
- (WWW 2025) **AERO: Enhancing Sharding Blockchain via Deep Reinforcement Learning for Account Migration** [[Paper](https://doi.org/10.1145/3696410.3714926)] `RL` `Sharding` — *Blockchain Systems & Infrastructure*
- (WWW 2025) **Beyond Visual Confusion: Understanding How Inconsistencies in ENS Normalization Facilitate Homoglyph Attacks** [[Paper](https://doi.org/10.1145/3696410.3714675)] `Measurement` · *ENS* — *NFT, DAO & Web3 Ecosystem*
- (WWW 2025) **CATALOG: Exploiting Joint Temporal Dependencies for Enhanced Phishing Detection on Ethereum** [[Paper](https://doi.org/10.1145/3696410.3714903)] `Temporal-Graph` · *Ethereum* — *Fraud, Scam & Attack Detection*
- (WWW 2025) **Fully Anonymous Decentralized Identity Supporting Threshold Traceability with Practical Blockchain** [[Paper](https://doi.org/10.1145/3696410.3714762)] `Cryptography` · *DID* — *NFT, DAO & Web3 Ecosystem*
- (WWW 2025) **Gamblers or Delegatees: Identifying Hidden Participant Roles in Crypto Casinos** [[Paper](https://doi.org/10.1145/3696410.3714689)] `Measurement` · *Crypto* — *On-chain Transaction & Graph Analytics*
- (WWW 2025) **Hunting in the Dark Forest: A Pre-trained Model for On-chain Attack Transaction Detection in Web3** [[Paper](https://doi.org/10.1145/3696410.3714928)] [[Code](https://github.com/wuzhy1ng/attack_trans_detection_www25)] `Pre-training` `Transformer` · *EVM* — *Fraud, Scam & Attack Detection*
- (WWW 2025) **Linking Souls to Humans: Blockchain Accounts with Credible Anonymity for Web 3.0 Decentralized Identity** [[Paper](https://doi.org/10.1145/3696410.3714784)] `Cryptography` · *DID* — *NFT, DAO & Web3 Ecosystem*
- (WWW 2025) **MAP the Blockchain World: A Trustless and Scalable Blockchain Interoperability Protocol for Cross-chain Applications** [[Paper](https://doi.org/10.1145/3696410.3714867)] `Interoperability` · *Multi-chain* — *Blockchain Systems & Infrastructure*
- (WWW 2025) **NFTs as a Data-Rich Test Bed: Conspicuous Consumption and its Determinants** [[Paper](https://doi.org/10.1145/3696410.3714724)] `Economics` · *NFT* — *NFT, DAO & Web3 Ecosystem*
- (WWW 2025) **Private Order Flows and Builder Bidding Dynamics: The Road to Monopoly in Ethereum's Block Building Market** [[Paper](https://doi.org/10.1145/3696410.3714754)] `Measurement` `Game-Theory` · *Ethereum* — *DeFi, MEV & Market Mechanisms*
- (WWW 2025) **Quantitative Runtime Monitoring of Ethereum Transaction Attacks** [[Paper](https://doi.org/10.1145/3696410.3714682)] `Runtime-Verification` · *Ethereum* — *Smart Contract Security & Analysis*
- (WWW 2025) **Safeguarding Blockchain Ecosystem: Understanding and Detecting Attack Transactions on Cross-chain Bridges** [[Paper](https://doi.org/10.1145/3696410.3714604)] `Measurement` · *Cross-chain* — *Fraud, Scam & Attack Detection*
- (WWW 2025) **Serial Scammers and Attack of the Clones: How Scammers Coordinate Multiple Rug Pulls on Decentralized Exchanges** [[Paper](https://doi.org/10.1145/3696410.3714919)] `Measurement` · *DEX* — *Fraud, Scam & Attack Detection*
- (WWW 2025) **SigScope: Detecting and Understanding Off-Chain Message Signing-related Vulnerabilities in Decentralized Applications** [[Paper](https://doi.org/10.1145/3696410.3714686)] `Program-Analysis` · *DApp* — *Smart Contract Security & Analysis*
- (WWW 2025) **SuiGPT MAD: Move AI Decompiler to Improve Transparency and Auditability on Non-Open-Source Blockchain Smart Contract** [[Paper](https://doi.org/10.1145/3696410.3714790)] `LLM` · *Sui* — *Smart Contract Security & Analysis*
- (WWW 2025) **The Poorest Man in Babylon: A Longitudinal Study of Cryptocurrency Investment Scams** [[Paper](https://doi.org/10.1145/3696410.3714588)] `Measurement` · *Crypto* — *Fraud, Scam & Attack Detection*
- (WWW 2025 Companion) **Bridging Culture and Finance: A Multimodal Analysis of Memecoins in the Web3 Ecosystem** [[Paper](https://doi.org/10.1145/3701716.3715561)] [[Code](https://github.com/hwlongCUHK/Coin-Meme)] `Multimodal` · *Memecoin* — *NFT, DAO & Web3 Ecosystem*
- (WWW 2025 Companion) **HedgeAgents: A Balanced-aware Multi-agent Financial Trading System** ＊ [[Paper](https://doi.org/10.1145/3701716.3715232)] [[Code](https://github.com/hedgeagents/hedgeagents.github.io)] `LLM` `Agent` · *Crypto* — *Trading & Portfolio Management*
- (AAAI 2025) **CLEP: A Novel Contrastive Learning Method for Evolutionary Reentrancy Vulnerability Detection** [[Paper](https://doi.org/10.1609/aaai.v39i1.31981)] `Contrastive` · *Ethereum* — *Smart Contract Security & Analysis*
- (AAAI 2025) **MTVHunter: Smart Contracts Vulnerability Detection Based on Multi-Teacher Knowledge Translation** [[Paper](https://doi.org/10.1609/aaai.v39i14.33664)] [[Code](https://github.com/KD-SCVD/MTVHunter)] `Knowledge-Distillation` · *Ethereum* — *Smart Contract Security & Analysis*
- (AAAI 2025) **SCALM: Detecting Bad Practices in Smart Contracts Through LLMs** [[Paper](https://doi.org/10.1609/aaai.v39i1.32026)] `LLM` · *Ethereum* — *Smart Contract Security & Analysis*
- (IJCAI 2025) **Airdrop Games** [[Paper](https://doi.org/10.24963/ijcai.2025/431)] `Game-Theory` · *Token* — *DeFi, MEV & Market Mechanisms*
- (IJCAI 2025) **Guiding LLM-based Smart Contract Generation with Finite State Machine** [[Paper](https://doi.org/10.24963/ijcai.2025/653)] `LLM` · *Ethereum* — *Smart Contract Security & Analysis*
- (IJCAI 2025) **Smart Contracts for Trustless Sampling of Correlated Equilibria** [[Paper](https://doi.org/10.24963/ijcai.2025/416)] `Game-Theory` · *Ethereum* — *DeFi, MEV & Market Mechanisms*
- (CIKM 2025) **Adaptive Bidirectional State Space Model for High-frequency Portfolio Management** ＊ [[Paper](https://doi.org/10.1145/3746252.3761246)] `SSM` `RL` · *Crypto* — *Trading & Portfolio Management*
- (CIKM 2025) **CoinCLIP: A Multimodal Framework for Assessing Viability in Web3 Memecoins** [[Paper](https://doi.org/10.1145/3746252.3760881)] `Multimodal` · *Memecoin* — *NFT, DAO & Web3 Ecosystem*
- (CIKM 2025) **From Patterns to Predictions: A Shapelet-Based Framework for Directional Forecasting in Noisy Financial Markets** ＊ [[Paper](https://doi.org/10.1145/3746252.3761250)] `Shapelet` `Time-Series` · *Bitcoin* — *Price Forecasting & Market Analysis*
- (ICDM 2025) **Equilibrium-Based NFT Marketplace Recommendation for NFTs with Breeding** [[Paper](https://doi.org/10.1109/icdm65498.2025.00094)] [[Code](https://github.com/jimmy-academia/BANTER)] `Recommendation` `Game-Theory` · *NFT* — *NFT, DAO & Web3 Ecosystem*
- (ICDM 2025) **When LLM Meets Simplicial Complex: A Novel Graph Prompt Learning on Ethereum Transaction Networks** [[Paper](https://doi.org/10.1109/icdm65498.2025.00148)] `LLM` `GNN` · *Ethereum* — *On-chain Transaction & Graph Analytics*
- (ICDE 2025) **E³FS: Efficient, Secure, and Verifiable Fuzzy Search with Data Updates in Hybrid-Storage Blockchains** [[Paper](https://doi.org/10.1109/icde65448.2025.00290)] `Query-Processing` — *Blockchain Systems & Infrastructure*
- (ICDE 2025) **Know Your Account: Double Graph Inference-Based Account De-Anonymization on Ethereum** [[Paper](https://doi.org/10.1109/icde65448.2025.00102)] `GNN` · *Ethereum* — *On-chain Transaction & Graph Analytics*
- (ICDE 2025) **Loom: A Deterministic Execution Framework Towards Nested Contract Transactions** [[Paper](https://doi.org/10.1109/icde65448.2025.00182)] `Concurrency` · *Permissioned* — *Blockchain Systems & Infrastructure*
- (ICDE 2025) **MEST: An Efficient Authenticated Secondary Index in Blockchain Systems** [[Paper](https://doi.org/10.1109/icde65448.2025.00126)] `Indexing` — *Blockchain Systems & Infrastructure*
- (ICDE 2025) **Towards Dynamic Boolean Range Query Over Hybrid-Storage Blockchains: A Secure and Reliably Verifiable Framework** [[Paper](https://doi.org/10.1109/icde65448.2025.00128)] `Query-Processing` — *Blockchain Systems & Infrastructure*
- (ICDE 2025) **VGQ: Enabling Verifiable Graph Queries on Blockchain Systems** [[Paper](https://doi.org/10.1109/icde65448.2025.00269)] `Query-Processing` — *Blockchain Systems & Infrastructure*
- (WSDM 2025) **Optimizing Blockchain Analysis: Tackling Temporality and Scalability with an Incremental Approach with Metropolis-Hastings Random Walks** [[Paper](https://doi.org/10.1145/3701551.3703521)] `Graph-Sampling` · *Crypto* — *On-chain Transaction & Graph Analytics*
- (EMNLP 2025) **SolEval: Benchmarking Large Language Models for Repository-level Solidity Smart Contract Generation** [[Paper](https://doi.org/10.18653/v1/2025.emnlp-main.218)] [[Code](https://github.com/pzy2000/SolEval)] `LLM` · *Ethereum* — *Smart Contract Security & Analysis*

## 2024

- (NeurIPS 2024) **Detecting Bugs with Substantial Monetary Consequences by LLM and Rule-based Reasoning** [[Paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/f1d8400fec75f683c4d823f5836a81bb-Abstract-Conference.html)] `LLM` `Program-Analysis` · *Ethereum* — *Smart Contract Security & Analysis*
- (NeurIPS 2024 D&B) **Multi-Chain Graphs of Graphs: A New Approach to Analyzing Blockchain Datasets** [[Paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/3205b048f9cc54b9f7963db0b0f52d53-Abstract-Datasets_and_Benchmarks_Track.html)] [[Code](https://github.com/Xtra-Computing/Cryptocurrency-Graphs-of-graphs)] `GNN` · *Multi-chain* — *On-chain Transaction & Graph Analytics*
- (ICLR 2024) **EX-Graph: A Pioneering Dataset Bridging Ethereum and X** [[Paper](https://openreview.net/forum?id=juE0rWGCJW)] `GNN` · *Ethereum* — *On-chain Transaction & Graph Analytics*
- (KDD 2024) **BitLINK: Temporal Linkage of Address Clusters in Bitcoin Blockchain** [[Paper](https://doi.org/10.1145/3637528.3672037)] `Clustering` · *Bitcoin* — *On-chain Transaction & Graph Analytics*
- (KDD 2024) **COMET: NFT Price Prediction with Wallet Profiling** [[Paper](https://doi.org/10.1145/3637528.3671621)] `Time-Series` `Graph` · *NFT* — *Price Forecasting & Market Analysis*
- (KDD 2024) **MacroHFT: Memory Augmented Context-aware Reinforcement Learning On High Frequency Trading** [[Paper](https://doi.org/10.1145/3637528.3672064)] [[Code](https://github.com/ZONG0004/MacroHFT)] `RL` · *Crypto* — *Trading & Portfolio Management*
- (KDD 2024) **Money Never Sleeps: Maximizing Liquidity Mining Yields in Decentralized Finance** [[Paper](https://doi.org/10.1145/3637528.3671942)] `Optimization` · *DeFi* — *DeFi, MEV & Market Mechanisms*
- (KDD 2024) **The Fourth International Workshop on Smart Data for Blockchain and Distributed Ledger (SDBD'24)** [[Paper](https://doi.org/10.1145/3637528.3671475)] `Workshop` — *Surveys, Tutorials & Workshops*
- (WWW 2024) **Advancing Web 3.0: Making Smart Contracts Smarter on Blockchain** [[Paper](https://doi.org/10.1145/3589334.3645319)] `AI-Inference` `Systems` · *Ethereum* — *Blockchain Systems & Infrastructure*
- (WWW 2024) **ARTEMIS: Detecting Airdrop Hunters in NFT Markets with a Graph Learning System** [[Paper](https://doi.org/10.1145/3589334.3645597)] `GNN` · *NFT* — *Fraud, Scam & Attack Detection*
- (WWW 2024) **Blockchain Censorship** [[Paper](https://doi.org/10.1145/3589334.3645431)] `Measurement` · *Ethereum* — *Blockchain Systems & Infrastructure*
- (WWW 2024) **Characterizing Ethereum Upgradable Smart Contracts and Their Security Implications** [[Paper](https://doi.org/10.1145/3589334.3645640)] `Measurement` · *Ethereum* — *Smart Contract Security & Analysis*
- (WWW 2024) **DenseFlow: Spotting Cryptocurrency Money Laundering in Ethereum Transaction Graphs** [[Paper](https://doi.org/10.1145/3589334.3645692)] `Graph-Mining` · *Ethereum* — *Fraud, Scam & Attack Detection*
- (WWW 2024) **Exploring Unconfirmed Transactions for Effective Bitcoin Address Clustering** [[Paper](https://doi.org/10.1145/3589334.3645684)] `Clustering` · *Bitcoin* — *On-chain Transaction & Graph Analytics*
- (WWW 2024) **IDEA-DAC: Integrity-Driven Editing for Accountable Decentralized Anonymous Credentials via ZK-JSON** [[Paper](https://doi.org/10.1145/3589334.3645658)] [[Code](https://github.com/Nullus-Labs/IDEA-DAC)] `Cryptography` · *DID* — *NFT, DAO & Web3 Ecosystem*
- (WWW 2024) **Identifying Risky Vendors in Cryptocurrency P2P Marketplaces** [[Paper](https://doi.org/10.1145/3589334.3645475)] `Machine-Learning` · *Crypto* — *Fraud, Scam & Attack Detection*
- (WWW 2024) **Interface Illusions: Uncovering the Rise of Visual Scams in Cryptocurrency Wallets** [[Paper](https://doi.org/10.1145/3589334.3645348)] `Measurement` · *Wallet* — *Fraud, Scam & Attack Detection*
- (WWW 2024) **Investigations of Top-Level Domain Name Collisions in Blockchain Naming Services** [[Paper](https://doi.org/10.1145/3589334.3645459)] `Measurement` · *ENS* — *NFT, DAO & Web3 Ecosystem*
- (WWW 2024) **SPRING: Improving the Throughput of Sharding Blockchain via Deep Reinforcement Learning Based State Placement** [[Paper](https://doi.org/10.1145/3589334.3645386)] `RL` `Sharding` — *Blockchain Systems & Infrastructure*
- (WWW 2024) **Unveiling the Paradox of NFT Prosperity** [[Paper](https://doi.org/10.1145/3589334.3645566)] `Measurement` · *NFT* — *NFT, DAO & Web3 Ecosystem*
- (WWW 2024) **ZipZap: Efficient Training of Language Models for Large-Scale Fraud Detection on Blockchain** [[Paper](https://doi.org/10.1145/3589334.3645352)] [[Code](https://github.com/git-disl/ZipZap)] `Transformer` `Pre-training` · *Ethereum* — *Fraud, Scam & Attack Detection*
- (WWW 2024 Companion) **Anonymity Analysis of the Umbra Stealth Address Scheme on Ethereum** [[Paper](https://doi.org/10.1145/3589335.3651963)] `Privacy` · *Ethereum* — *On-chain Transaction & Graph Analytics*
- (WWW 2024 Companion) **CAAW'24: The 3rd International Cryptoasset Analytics Workshop** [[Paper](https://doi.org/10.1145/3589335.3641304)] `Workshop` — *Surveys, Tutorials & Workshops*
- (WWW 2024 Companion) **Characterizing the Solana NFT Ecosystem** [[Paper](https://doi.org/10.1145/3589335.3651478)] `Measurement` · *Solana, NFT* — *NFT, DAO & Web3 Ecosystem*
- (WWW 2024 Companion) **Concentration of Power and Participation in Online Governance: the Ecosystem of Decentralized Autonomous Organizations** [[Paper](https://doi.org/10.1145/3589335.3651481)] `Measurement` · *DAO* — *NFT, DAO & Web3 Ecosystem*
- (WWW 2024 Companion) **Deanonymizing Transactions Originating from Monero Tor Hidden Service Nodes** [[Paper](https://doi.org/10.1145/3589335.3651487)] `Privacy` · *Monero* — *On-chain Transaction & Graph Analytics*
- (WWW 2024 Companion) **DeFiTail: DeFi Protocol Inspection through Cross-Contract Execution Analysis** [[Paper](https://doi.org/10.1145/3589335.3651488)] `Program-Analysis` · *DeFi* — *Smart Contract Security & Analysis*
- (WWW 2024 Companion) **Detecting Financial Bots on the Ethereum Blockchain** [[Paper](https://doi.org/10.1145/3589335.3651959)] `Machine-Learning` · *Ethereum* — *Fraud, Scam & Attack Detection*
- (WWW 2024 Companion) **Distributed Transparent Data Layer for Next Generation Blockchains** [[Paper](https://doi.org/10.1145/3589335.3651255)] `Systems` — *Blockchain Systems & Infrastructure*
- (WWW 2024 Companion) **Incentives in the Ether: Practical Cryptocurrency Economics & Security** [[Paper](https://doi.org/10.1145/3589335.3651268)] `Tutorial` — *Surveys, Tutorials & Workshops*
- (WWW 2024 Companion) **Measuring Arbitrage Losses and Profitability of AMM Liquidity** [[Paper](https://doi.org/10.1145/3589335.3651961)] `Measurement` · *DEX* — *DeFi, MEV & Market Mechanisms*
- (WWW 2024 Companion) **Seamlessly Transferring Assets through Layer-0 Bridges: An Empirical Analysis of Stargate Bridge's Architecture and Dynamics** [[Paper](https://doi.org/10.1145/3589335.3651964)] `Measurement` · *Cross-chain* — *Blockchain Systems & Infrastructure*
- (WWW 2024 Companion) **StateGuard: Detecting State Derailment Defects in Decentralized Exchange Smart Contract** [[Paper](https://doi.org/10.1145/3589335.3651562)] `Program-Analysis` · *DEX* — *Smart Contract Security & Analysis*
- (WWW 2024 Companion) **Statistical Confidence in Mining Power Estimates for PoW Blockchains** [[Paper](https://doi.org/10.1145/3589335.3651960)] `Statistics` · *PoW* — *Blockchain Systems & Infrastructure*
- (WWW 2024 Companion) **Towards Understanding Crypto-Asset Risks on Ethereum Caused by Key Leakage on the Internet** [[Paper](https://doi.org/10.1145/3589335.3651573)] `Measurement` · *Ethereum* — *Fraud, Scam & Attack Detection*
- (WWW 2024 Companion) **Unveiling Wash Trading in Popular NFT Markets** [[Paper](https://doi.org/10.1145/3589335.3651580)] `Measurement` · *NFT* — *Fraud, Scam & Attack Detection*
- (WWW 2024 Companion) **When Crypto Economics Meet Graph Analytics and Learning** [[Paper](https://doi.org/10.1145/3589335.3651257)] `Tutorial` — *Surveys, Tutorials & Workshops*
- (AAAI 2024) **Approval-Based Committee Voting in Practice: A Case Study of (over-)Representation in the Polkadot Blockchain** [[Paper](https://doi.org/10.1609/aaai.v38i9.28807)] `Social-Choice` · *Polkadot* — *Blockchain Systems & Infrastructure*
- (AAAI 2024) **EarnHFT: Efficient Hierarchical Reinforcement Learning for High Frequency Trading** [[Paper](https://doi.org/10.1609/aaai.v38i13.29384)] [[Code](https://github.com/TradeMaster-NTU/EarnHFT)] `RL` · *Crypto* — *Trading & Portfolio Management*
- (IJCAI 2024) **EFEVD: Enhanced Feature Extraction for Smart Contract Vulnerability Detection** [[Paper](https://doi.org/10.24963/ijcai.2024/469)] `Deep-Learning` `Vulnerability-Detection` · *Ethereum* — *Smart Contract Security & Analysis*
- (IJCAI 2024) **Survey on Strategic Mining in Blockchain: A Reinforcement Learning Approach** [[Paper](https://doi.org/10.24963/ijcai.2024/1170)] `RL` `Survey` — *Surveys, Tutorials & Workshops*
- (IJCAI 2024) **Trade When Opportunity Comes: Price Movement Forecasting via Locality-Aware Attention and Iterative Refinement Labeling** ＊ [[Paper](https://doi.org/10.24963/ijcai.2024/678)] `Transformer` · *Crypto* — *Price Forecasting & Market Analysis*
- (CIKM 2024) **Cryptocurrency Price Forecasting using Variational Autoencoder with Versatile Quantile Modeling** [[Paper](https://doi.org/10.1145/3627673.3680027)] `Generative` `Time-Series` · *Crypto* — *Price Forecasting & Market Analysis*
- (CIKM 2024) **Effective Illicit Account Detection on Large Cryptocurrency MultiGraphs** [[Paper](https://doi.org/10.1145/3627673.3679707)] [[Code](https://github.com/TommyDzh/DIAM)] `GNN` · *Crypto* — *Fraud, Scam & Attack Detection*
- (CIKM 2024) **HTFabric: A Fast Re-ordering and Parallel Re-execution Method for a High-Throughput Blockchain** [[Paper](https://doi.org/10.1145/3627673.3679606)] [[Code](https://github.com/jaeyubsong/HTFabric)] `Systems` · *Permissioned* — *Blockchain Systems & Infrastructure*
- (ICDE 2024) **Authenticated Keyword Search on Large-Scale Graphs in Hybrid-Storage Blockchains** [[Paper](https://doi.org/10.1109/icde60146.2024.00155)] `Query-Processing` — *Blockchain Systems & Infrastructure*
- (ICDE 2024) **Authenticated Subgraph Matching in Hybrid-Storage Blockchains** [[Paper](https://doi.org/10.1109/icde60146.2024.00159)] `Query-Processing` — *Blockchain Systems & Infrastructure*
- (ICDE 2024) **Efficient Partial Order Based Transaction Processing for Permissioned Blockchains** [[Paper](https://doi.org/10.1109/icde60146.2024.00152)] `Systems` · *Permissioned* — *Blockchain Systems & Infrastructure*
- (ICDE 2024) **Enabling Efficient, Verifiable, and Secure Conjunctive Keyword Search in Hybrid-Storage Blockchains** [[Paper](https://doi.org/10.1109/icde60146.2024.00481)] `Query-Processing` — *Blockchain Systems & Infrastructure*
- (ICDE 2024) **MuFuzz: Sequence-Aware Mutation and Seed Mask Guidance for Blockchain Smart Contract Fuzzing** [[Paper](https://doi.org/10.1109/icde60146.2024.00158)] [[Code](https://github.com/OMH4ck/mufuzz)] `Fuzzing` · *Ethereum* — *Smart Contract Security & Analysis*
- (ICDE 2024) **Porygon: Scaling Blockchain via 3D Parallelism** [[Paper](https://doi.org/10.1109/icde60146.2024.00153)] `Systems` — *Blockchain Systems & Infrastructure*
- (ICDE 2024) **SharDAG: Scaling DAG-Based Blockchains Via Adaptive Sharding** [[Paper](https://doi.org/10.1109/icde60146.2024.00165)] `Sharding` — *Blockchain Systems & Infrastructure*
- (ICDE 2024) **SpotLess: Concurrent Rotational Consensus Made Practical Through Rapid View Synchronization** [[Paper](https://doi.org/10.1109/icde60146.2024.00157)] `Consensus` — *Blockchain Systems & Infrastructure*
- (ICDE 2024) **TELL: Efficient Transaction Execution Protocol Towards Leaderless Consensus** [[Paper](https://doi.org/10.1109/icde60146.2024.00154)] `Consensus` · *Permissioned* — *Blockchain Systems & Infrastructure*
- (ICDE 2024) **V2FS : A Verifiable Virtual Filesystem for Multi-Chain Query Authentication** [[Paper](https://doi.org/10.1109/icde60146.2024.00160)] `Query-Processing` · *Multi-chain* — *Blockchain Systems & Infrastructure*
- (EMNLP 2024) **CryptoTrade: A Reflective LLM-based Agent to Guide Zero-shot Cryptocurrency Trading** [[Paper](https://doi.org/10.18653/v1/2024.emnlp-main.63)] [[Code](https://github.com/Xtra-Computing/CryptoTrade)] `LLM` `Agent` · *Crypto* — *Trading & Portfolio Management*

# Datasets & Benchmarks

[Back to top](#table-of-contents)

Papers that release a dataset or benchmark (also listed under their task above).

- (ICML 2026) **EVMbench: Evaluating AI Agents on Smart Contract Security** [[Paper](https://openreview.net/forum?id=K5S8N5NgD8)] [[Code](https://github.com/paradigmxyz/evmbench)] `LLM` `Agent` · *Ethereum*
- (ICLR 2026) **CTBench: Cryptocurrency Time Series Generation Benchmark** [[Paper](https://openreview.net/forum?id=RzT2sombPD)] `Generative` `Time-Series` · *Crypto*
- (KDD 2026) **DMind Benchmark: Toward a Holistic Assessment of LLM Capabilities across the Web3 Domain** [[Paper](https://doi.org/10.1145/3770855.3817512)] `LLM` · *Web3*
- (WWW 2026 Companion) **Benchmarking Temporal Web3 Intelligence: Lessons from the FinSurvival 2025 Challenge** [[Paper](https://doi.org/10.1145/3774905.3795449)] `Survival-Analysis` · *DeFi*
- (ACL 2026) **EVM-QuestBench: An Execution-Grounded Benchmark for Natural-Language Transaction Code Generation** [[Paper](https://doi.org/10.18653/v1/2026.acl-long.1642)] [[Code](https://github.com/OpenEdgeHQ/EVM-quest-bench)] `LLM` · *Ethereum*
- (NeurIPS 2025 D&B) **MiNT: Multi-Network Transfer Benchmark for Temporal Graph Learning** [[Paper](https://openreview.net/forum?id=Za7IcsXIRV)] [[Code](https://github.com/benjaminnNgo/ScalingTGNs)] `Temporal-Graph` `Transfer-Learning` · *Ethereum*
- (NeurIPS 2025 D&B) **The Temporal Graph of Bitcoin Transactions** [[Paper](https://openreview.net/forum?id=Xs7JM4VGHv)] [[Code](https://github.com/B1AAB/EBA)] `Temporal-Graph` · *Bitcoin*
- (ICLR 2025 Workshop) **FinTSBridge: A New Evaluation Suite for Real-world Financial Prediction with Advanced Time Series Models** ＊ [[Paper](https://arxiv.org/abs/2503.06928)] `Time-Series` · *Crypto*
- (EMNLP 2025) **SolEval: Benchmarking Large Language Models for Repository-level Solidity Smart Contract Generation** [[Paper](https://doi.org/10.18653/v1/2025.emnlp-main.218)] [[Code](https://github.com/pzy2000/SolEval)] `LLM` · *Ethereum*
- (NeurIPS 2024 D&B) **Multi-Chain Graphs of Graphs: A New Approach to Analyzing Blockchain Datasets** [[Paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/3205b048f9cc54b9f7963db0b0f52d53-Abstract-Datasets_and_Benchmarks_Track.html)] [[Code](https://github.com/Xtra-Computing/Cryptocurrency-Graphs-of-graphs)] `GNN` · *Multi-chain*
- (ICLR 2024) **EX-Graph: A Pioneering Dataset Bridging Ethereum and X** [[Paper](https://openreview.net/forum?id=juE0rWGCJW)] `GNN` · *Ethereum*

# How to Contribute

This list is updated continuously, and contributions are welcome.

**Requirement**: The paper is accepted at one of the conferences listed at the top.

**Steps**:

1. Fork this repository and clone your fork.
2. Push to your fork and open a pull request.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the entry format.

# License

Released under the [Apache License 2.0](LICENSE).

<div align="center">

If you find this list useful, please consider giving it a star. It helps others discover these papers.

</div>
