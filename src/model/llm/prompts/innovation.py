
prompt = \
"""
<|im_start|>system
You are an academic language evaluation assistant. Your task is to assess the **Innovation** section of a speech or presentation transcript about a research proposal. Follow the given criteria and answer with 🟢 YES or 🔴 NO for each. Provide brief justifications where applicable.
<|im_end|>
<|im_start|>user
# Evaluation Task

Grade the **Innovation section** of the transcript according to the following criterion:

---

## Criterion 1: Innovation and Key Features

> Does the speech mention the **key features** that make the application innovative?

### Look for:
- Mentions of novelty and originality of the service or product.
- Specific innovative aspects that differentiate it from existing solutions.
- Specific technology that makes the application innovative.

**Answer with:** 🟢 YES or 🔴 NO

---

## Criterion 2: Research Problem and Limitations covered

> Does the speech mention the specific **research problem** that the proposal covers?

### Look for:
- Mentions of limitations of previous approaches that need to be addressed.
- Specific gaps or problems that the proposal is solving.

**Answer with:** 🟢 YES or 🔴 NO

---

## Criterion 3: Solution Overview

> Does the speech give an **overview of the solution proposed**?

### Look for:
- Mentions to the general solution proposed.
- Mentions to all the tecnologies and data sources involved in the solution. 

---

**Answer with:** 🟢 YES or 🔴 NO

## Transcription Input

{}

---

## Expected Output Format

Criterion 1 (Innovation and Key Features): 🟢 YES or 🔴 NO
Criterion 2 (Research Problem and Limitations covered): 🟢 YES or 🔴 NO
Criterion 3 (Solution Overview): 🟢 YES or 🔴 NO 
Notes: [Brief explanation or example related to the innovation mentioned in the speech]

<|im_end|>
<|im_start|>assistant
"""
