---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign gsStatsUrl = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

## About Me

I am a Ph.D. student in Computer Science at [Rutgers University](https://www.rutgers.edu/), advised by Prof. [Zheng (Eddy) Z. Zhang](https://people.cs.rutgers.edu/zz124/). My research lies at the intersection of **quantum computing systems**, **compiler optimization**, and **artificial intelligence**, with the goal of making quantum programs easier to construct, optimize, and execute.

My current work focuses on compilation and optimization for quantum applications, particularly Hamiltonian simulation and hybrid continuous-variable/discrete-variable quantum computing. I am also interested in using machine learning and large language models to improve quantum circuit synthesis, optimization, and scientific reasoning.

Before joining Rutgers, I received my B.S. in Computer Science from Lanzhou University, where I worked with Prof. [Yonggang Lu](https://www.researchgate.net/profile/Yonggang-Lu) on graph machine learning and community detection. I also worked with Prof. [Fajie Yuan](https://fajieyuan.github.io/) at Westlake University on deep learning for biological applications.

[![Google Scholar Citations](https://img.shields.io/endpoint?url={{ gsStatsUrl | url_encode }}&logo=Google%20Scholar&label=Citations&color=4285F4&style=flat-square)](https://scholar.google.com/citations?user=FVJO7aAAAAAJ&hl=en)

## Research Interests

* **Quantum compilation and system software**, including compilation from physical Hamiltonians to executable quantum circuits.
* **Hamiltonian simulation**, especially for fermionic systems and hybrid CV-DV quantum architectures.
* **AI-assisted quantum circuit synthesis and optimization**, including machine-learning- and LLM-guided methods.
* **AI for scientific discovery**, with applications in quantum computing, graphs, and computational biology.

## News

* **Jun. 2025:** Our paper **Genesis** was presented at ISCA 2025 in Tokyo, Japan.
* **May 2025:** Received an **ISCA Student Travel Award**.
* **Jul. 2024:** Our survey on community detection was published in *Neurocomputing*.

## Publications

<sup>†</sup> Equal contribution. <sup>*</sup> Corresponding author.

### 2025

**[Genesis: A Compiler for Hamiltonian Simulation on Hybrid CV-DV Quantum Computers](https://dl.acm.org/doi/10.1145/3695053.3731065)**
Zihan Chen<sup>†</sup>, **Jiakang Li<sup>†</sup>**, Minghao Guo<sup>†</sup>, Henry Chen, Zirui Li, Joel Bierman, Yipeng Huang, Huiyang Zhou, Yuan Liu, and Eddy Z. Zhang
*Proceedings of the 52nd Annual International Symposium on Computer Architecture* (**ISCA 2025**), pp. 1583–1597.
[[Paper](https://dl.acm.org/doi/10.1145/3695053.3731065)]
[[arXiv](https://arxiv.org/abs/2505.13683)]
[[Code](https://github.com/ruadapt/Genesis-CVDV-Compiler)]

### 2024

**[A Comprehensive Review of Community Detection in Graphs](https://www.sciencedirect.com/science/article/pii/S0925231224009408)**
**Jiakang Li<sup>†</sup>**, Songning Lai<sup>†</sup>, Zhihao Shuai, Yuan Tan, Yifan Jia, Mianyang Yu, Zichen Song, Xiaokang Peng, Ziyang Xu, Yongxin Ni, Haifeng Qiu, Jiayu Yang, Yutong Liu, and Yonggang Lu<sup>*</sup>
*Neurocomputing*, Volume 600, Article 128169, 2024.
[[Paper](https://www.sciencedirect.com/science/article/pii/S0925231224009408)]
[[arXiv](https://arxiv.org/abs/2309.11798)]

### 2023

**[Community Detection Using Revised Medoid-Shift Based on KNN](https://link.springer.com/chapter/10.1007/978-981-99-4752-2_29)**
**Jiakang Li**, Xiaokang Peng, Jie Hou, Wei Ke, and Yonggang Lu<sup>*</sup>
*International Conference on Intelligent Computing* (**ICIC 2023**).

## Research Experience

### Rutgers University

**Graduate Research Assistant**
*Sep. 2024–Present · Piscataway, New Jersey*

* Advised by Prof. [Zheng (Eddy) Z. Zhang](https://people.cs.rutgers.edu/zz124/).
* Conduct research on quantum computing systems, Hamiltonian simulation, and quantum compilation.
* Develop compiler techniques for mapping physical Hamiltonians to executable programs on emerging quantum architectures.
* Explore machine-learning- and LLM-assisted approaches for quantum circuit optimization.

### Westlake University

**Research Intern**
*Apr. 2023–Nov. 2023 · Hangzhou, China*

* Advised by Prof. [Fajie Yuan](https://fajieyuan.github.io/).
* Studied AI-for-Science problems involving protein–protein interaction prediction.
* Developed deep learning methods for learning representations from biological data.

### Lanzhou University

**Undergraduate Researcher**
*Jan. 2022–Apr. 2023 · Lanzhou, China*

* Advised by Prof. [Yonggang Lu](https://www.researchgate.net/profile/Yonggang-Lu).
* Studied clustering algorithms and graph-based community detection.
* Conducted empirical comparisons of classical, probabilistic, spectral, and deep-learning-based community detection methods.

## Industry Experience

### [Trip.com Group](https://www.trip.com/)

**Machine Learning Algorithm Intern**
*Jun. 2022–Oct. 2022 · Shanghai, China*

* Developed machine learning models for airfare price prediction.
* Worked on risk-control models for detecting potentially malicious users.
* Trained a detection model that achieved approximately 90% precision in the target evaluation setting.

## Education

### Rutgers University

**Ph.D. in Computer Science**
*Sep. 2024–Present*

Research areas: quantum computing systems, compiler optimization, and AI for quantum computing.

### Lanzhou University

**B.S. in Computer Science**
*Sep. 2019–Jun. 2023*

* GPA ranking: Top 13%.
* Affiliated with the Center for Computer Software and Theory.

### Additional Study

* **University of California, Berkeley** — Exchange Student, Jan.–Jun. 2021.
* **Massachusetts Institute of Technology** — Winter Course in Vision Science, Jan.–Feb. 2021.

## Teaching

* **Teaching Assistant**, CS 461: Machine Learning Principles, Rutgers University, Fall 2025.
* **Teaching Assistant**, CS 415: Compilers, Rutgers University, Spring 2025.
* **Teaching Assistant**, CS 206: Discrete Structures, Rutgers University, Fall 2024.

## Academic Service

* Reviewer, **IEEE International Conference on Multimedia and Expo (ICME 2025)**.
* Reviewer, **International Joint Conference on Neural Networks (IJCNN 2025)**.

## Honors and Awards

* **ISCA Student Travel Award**, 2025.
* **Lanzhou University Third-Class Scholarship**, 2022.
* **Lanzhou University Second-Class Scholarship**, 2021.
* **Lanzhou University Second-Class Scholarship**, 2020.
* **University-Level Academic Excellence Award**, 2020, 2021, and 2022.

## Beyond Research

Outside research, I enjoy competitive MOBA games, singing, and community building. I also create content about *Arena of Valor* and other MOBA games.

I am the founder of the [Lanzhou University Flyer organization](https://lzufly.github.io/), a student-led initiative that connects current students with alumni and shares information about graduate study, career development, and international opportunities.

I enjoy meeting people with different backgrounds and exploring new research ideas. Feel free to reach out if you would like to discuss quantum computing, AI for science, academic collaboration, or shared interests.
