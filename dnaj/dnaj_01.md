{% include head.html %}
![Hanze](../hanze/hanze.png)

[Go back to the main page](../index.md)

# DNAJ

---

## Introduction

Huntington’s disease is a fatal neurodegenerative disorder caused by a genetic mutation that produces an expanded polyglutamine tract in the Huntingtin protein. This mutation causes proteins to misfold and form toxic aggregates that destroy neurons in the brain. To manage this, cells utilize molecular chaperones, which act as a quality control system to ensure proper protein folding. These chaperones are essential for preventing the buildup of misfolded proteins and maintaining cellular health. Among these, DNAJ proteins, or Hsp40s, serve as vital co-chaperones that direct the activity of the Hsp70 folding machinery. They are identified by a conserved J-domain that allows them to bind specifically to client proteins.  

## What have we done?

We have studied specific molecular chaperones that effectively combat the misfolding and toxicity associated with polyglutamine diseases like Huntington's. We have engineered a series of tetracycline-inducible expression plasmids using the pcDNA5 FRT/TO vector system. By cloning various chaperone coding sequences in frame with a V5 tag, we have created fusion proteins to track expression and localization of these chaperones. Our cloning process utilized cDNA derived from a diverse pool of human cell lines and purchased full-length clones to ensure broad representation. We have cloned nearly all members of the HSP70, HSP110, DNAJA and DNAJB family (but not the DNAJC family). The library that we have created is accessible via [AddGene](https://www.addgene.org/search/catalog/plasmids/?q=kampinga+Hageman+et+al+Cell+Stress+Chaperones.+2009+Jan&page_number=4).  

![Pic](https://ars.els-cdn.com/content/image/1-s2.0-S1355814523018850-Fig2_HTML_lrg.jpg)
*<sub>The pcDNA5 FRT/TO vector system. [Source](https://www.sciencedirect.com/science/article/pii/S1355814523018850?via%3Dihub)</sub>*

After sequence verification and Western blot validation, the functional screening revealed that members of the DNAJB subclass (specifically DNAJB6b and DNAJB8) are exceptionally potent at suppressing protein aggregation and cellular toxicity. These findings highlight these specific DNAJ proteins as critical components of the cellular protein quality control network.  

![Pic](https://ars.els-cdn.com/content/image/1-s2.0-S1097276510000262-gr1_lrg.jpg)
*<sub>The result of the previous screen showing that DNAJB6b and DNAJB8 are the most effective suppressors of huntingtin aggregation. [Source](https://www.sciencedirect.com/science/article/pii/S1097276510000262?via%3Dihub)</sub>*

Identifying DNAJB6 as a suppressor was an important breakthrough because it's subsequent research provided mechanistic evidence of a chaperone that directly targets primary nucleation, the very first step of protein aggregation. DNAJB6 uses a specific serine/threonine-rich motif to bind and neutralize mutant Huntingtin "seeds" before they can multiply. DNAJB6’s ability to prevent the earliest stages of misfolding makes it a prime therapeutic target, as inducing its expression pharmaceutically could provide a natural cellular defense to reduce the progression of Huntington’s disease.  

DNAJB6 exists as a functional monomer or dimer that utilizes its J-domain to recruit HSP70 and a specific C-terminal motif to bind amyloid-prone clients. To increase its efficiency, it assembles into high-molecular-weight oligomeric "shells" that provide a high density of binding sites to trap disordered peptides. Once bound to a substrate, it forms a stable complex that effectively stalls the nucleation process, preventing the formation and spread of toxic protein aggregates.

![Pic](./pics/01.png)
*<sub>AlphaFold predicted structure of DNAJB6. Source: [AlphaFold server.](https://alphafoldserver.com/fold/6513fd66c075b29d)</sub>*

However, at the time, the DNAJC family (comprising 30 members) was to large and cumbersome to clone and screen.  

## What we want to do: cloning and screening the DNAJC family

We have cloned the HSP70, HSP110, DNAJA and DNAJB family. This was done more than 20 years ago. Generating the expression library was particularly cumbersome because it required cloning each chaperone gene from a diverse pool of cDNA's, a labor-intensive process of amplification and sequence verification for every individual candidate. Nowadays, the process is simplified because one can buy sequence verified cDNA sequences already clones in cloning vectors.  

We would like to expand our study by cloning and screening the DNAJC family. While some members like DNAJC5 and DNAJC13 are well-documented, the majority of the DNAJC subclass remains understudied and "less popular" in neurodegeneration research. The focus on a few genes has left a significant gap, as there is no systematic, head-to-head screen to rank the relative potency of these overlooked family members. Consequently, it remains unknown if these less-studied DNAJC proteins possess unique or superior abilities to suppress mutant Huntingtin toxicity.

We have already cloned a substantial amount of the library in the pcDNA5 FRT/TO vector system. See the table below. We would like to expand this study to buy and clone the remaining DNAJC members.

| DNAJ    | Alternative Name  | Cloned |
|---------|------------------ |--------|
| DNAJC1  | MTJ1, ERDJ1       | Yes    |
| DNAJC2  | MPP11, ZRF1       | No     |
| DNAJC3  | P58IPK            | Yes    |
| DNAJC4  | HSP40             | Yes    |
| DNAJC5  | CSP,CLN4, CLN4B   | No     |
| DNAJC5b | CSP-alpha         | Yes    |
| DNAJC5g | CSP-gamma         | Yes    |
| DNAJC6  | Auxilin-1         | Yes    |
| DNAJC7  | TPR2              | Yes    |
| DNAJC8  | HSPC331, SPF31    | No     |
| DNAJC9  | HDJC9, JDD1, SB73 | Yes    |
| DNAJC10 | ERDJ5             | No     |
| DNAJC11 | dJ126A5.1         | Yes    |
| DNAJC12 | JDP1              | Yes    |
| DNAJC13 | RME-8             | No     |
| DNAJC14 | DRIP78            | Yes    |
| DNAJC15 | MCJ               | Yes    |
| DNAJC16 | ERdj8             | Yes    |
| DNAJC17 | —                 | No     |
| DNAJC18 | —                 | Yes    |
| DNAJC19 | TIM14             | Yes    |
| DNAJC20 | HSCB              | No     |
| DNAJC21 | BMFS3, DNAJA5, GS3| No     |
| DNAJC22 | wus               | No     |
| DNAJC23 | SEC63, ERdj2      | No     |
| DNAJC24 | DPH4, JJJ3, ZCSL3 | Yes    |
| DNAJC25 | bA16L21.2.1       | Yes    |
| DNAJC26 | GAK               | No     |
| DNAJC27 | RBJ               | Yes    |
| DNAJC28 | C21orf55, C21orf78| No     |
| DNAJC29 | SACS, ARSACS      | No     |
| DNAJC30 | LHONAR, MC1DN38   | No     |

## Need for funding

Additional funding is required to clone the remaining DNAJC candidates and complete the systematic expression library for this subclass. Securing these resources will enable a comprehensive, head-to-head screen to identify the most effective therapeutic targets within the DNAJC family for Huntington’s disease. 

The expected costs are divided in two stages:

- Molecular Construction (Cloning & Synthesis). To complete the library, we would need to order the remaining ~14 DNAJC genes cloned from cDNA, subclone them in the pcDNA5 FRT/TO vector system and sequence the whole DNAJC library. This would cost approximately €5000 (materials).

- Systematic Screening (Cell-Based Assays)
Running a head-to-head screen across the full ~30-member DNAJC family requires high-throughput infrastructure. Reagents & Consumables: Specialized plates, transfection reagents, and slot-blot as well as imaging/quantification for Huntington’s aggregation. This would cost approximately €10000.

- Labor: Dedicated time for a PhD-level researcher and/or technician to optimize and execute the screen (3–6 months) is budgeted at $35,000.

Thus, the total costs are expected to be around $50,000.

---

You can find information about my cv [here](https://jurrehageman.github.io/cv/)

---

>This web page is distributed under the terms of the Creative Commons Attribution License which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.
>Creative Commons License: CC BY-SA 4.0.

