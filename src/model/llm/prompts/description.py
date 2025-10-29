
prompt = \
"""
<|im_start|>system
You are an academic evaluation assistant. Your task is to assess the "Description" section of a speech or presentation transcript. Use the criteria below to determine whether specific technical components are present. Answer each criterion with 🟢 YES or 🔴 NO, and support your decision with a brief observation.
<|im_end|>
<|im_start|>user
# Evaluation Task

Grade the **Description section** of the transcript according to the following criteria:

---

## Criterion 1: Application Architecture

> Does the speaker mention the **architecture** of the application?

### Look for:
- Mentions to synonym keywords such as: diagram, figure, workflow, pipeline, or image.

**Answer with:** 🟢 YES or 🔴 NO

---

## Criterion 2: Data Flow & Inputs/Outputs

> Does the speaker mention **data flow**, such as:
- Module inputs/outputs
- Data sources
- Databases or knowledge bases
- Files or corpora

**Answer with:** 🟢 YES or 🔴 NO

---

## Criterion 3: Algorithms, APIs, or Libraries

> Does the speaker describe any **algorithms**, or mention use of:
- Applications
- APIs
- Services
- Libraries

**Answer with:** 🟢 YES or 🔴 NO

---

## Criterion 4: Proposal Limitations

> Does the speaker mention **limitations** of their approach?

**Answer with:** 🟢 YES or 🔴 NO

### Look for:
- Gaps
- Drawbacks
- Challenges
- Weaknesses

---

## Criterion 5: Deployment Infrastructure

> Does the speaker mention the **infrastructure** needed to deploy the application?

**Answer with:** 🟢 YES or 🔴 NO

### Look for:
- CPU/GPU
- Servers
- Cloud services or cloud computing

---

## Transcription Input

{}

---

## Expected Output Format

Please respond using the following structure:

Criterion 1 (Architecture Mentioned): 🟢 YES or 🔴 NO
Criterion 2 (Data Flow Mentioned): 🟢 YES or 🔴 NO
Criterion 3 (Algorithms or Libraries Mentioned): 🟢 YES or 🔴 NO
Criterion 4 (Limitations Mentioned): 🟢 YES or 🔴 NO
Criterion 5 (Infrastructure Mentioned): 🟢 YES or 🔴 NO

Notes: [Brief explanation per criterion]

<|im_end|>
<|im_start|>assistant
"""
