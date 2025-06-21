# Social Network Analysis using Python & NetworkX

This project explores a **directed social‑interaction graph** built from a CSV survey of students.  
Each node in the graph is a student ID, and each directed edge indicates that one student listed another in their “impression” list.

The analysis is organised into **three independent questions**, each solved in its own Python script.

---

## 🔧 File Overview

### 1. `ques1.py` – Simulating PageRank via Random Walk  

* Builds a directed graph from `impressionNetwork.csv`.  
* Runs a **random walk with teleportation** (teleport‑probability = 0 .15, 100 000 steps).  
* Every time the walker lands on a node, that node earns a “coin.”  
* After the walk, the accumulated coins give a PageRank‑like **importance score** for each student.

---

### 2. `ques2.py` – Missing‑Link Detection  

* Examines every pair of nodes with **no edge in either direction**.  
* Uses the adjacency matrix and a **least‑squares approximation** to predict the likelihood of an edge.  
* If the predicted value exceeds **0 .5**, the pair is reported as a **potentially missing link**—useful for spotting hidden or forgotten interactions.

---

### 3. `ques3.py` – Community Density Analysis (CSB vs MCB)  

* Splits the big graph into two sub‑graphs by node label:  
  * **CSB_G** – nodes whose IDs contain “CSB”  
  * **MCB_G** – nodes whose IDs contain “MCB”  
* Adds edges to each sub‑graph only when both endpoints belong to that sub‑graph.  
* Computes the **edge‑density ratio**  

\[
r \;=\; 
\frac{\text{actual edges}}{n\,(n-1)}
\]

for both CSB and MCB, where \(n\) is the number of nodes in the sub‑graph.  
* Prints the two ratios so you can compare how densely each community interacts internally.

---

## 📁 Dataset — `impressionNetwork.csv`

The CSV file must sit in the same folder as the scripts.  
Structure (header row + 30 columns of impressions):

