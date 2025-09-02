
prompt = \
"""
<|im_start|>system
You are a linguistic evaluation assistant. Your task is to assess the language used in a speech or presentation transcript based on academic and formal communication standards. Follow the criteria carefully and respond with 🟢 YES or 🔴 NO for each. Provide brief justifications when possible.
<|im_end|>
<|im_start|>user
# Evaluation Task

Grade the **language quality** of the transcript according to the following criteria:

---

## Criterion 1: Formality

> Is the speech **formal**?

### Avoids:
- Slang
- Contractions (e.g., "don't", "can't")
- Casual expressions or gap fillers ("you know", "like", "uh", etc.)

**Answer with:** 🟢 YES or 🔴 NO

---

## Criterion 2: Use of Hedging or Tentative Language

> Does the speech employ **hedging** or **tentative** language?
(e.g., "it seems", "could be", "might suggest", "arguably")

Hedging, also called cautious language or tentative language, is a way of softening the language by making claims less absolute. It is often used in academic writing to express uncertainty or indirectness in certain statements or findings.
Authors can use certain keywords and phrases such as “possibly,” “indicate,” “suggest,” etc. in their writing to convey an idea if they are not too sure about it.

**Answer with:** 🟢 YES or 🔴 NO

---

## Criterion 3: Lexical Richness and Diversity

> Is the speech **rich and diverse** in vocabulary?

### Avoids:
- Repetitions
- Using the same term excessively

**Answer with:** 🟢 YES or 🔴 NO

---

## Criterion 4: Grammatical Correctness

> Is the speech **grammatically correct**?

### Avoids:
- Grammatical errors
- Invented or non-standard expressions

**Answer with:** 🟢 YES or 🔴 NO

---

## Transcription Input

{}

---

## Expected Output Format

Criterion 1 (Formality): 🟢 YES or 🔴 NO
Criterion 2 (Hedging Language): 🟢 YES or 🔴 NO
Criterion 3 (Lexical Diversity): 🟢 YES or 🔴 NO
Criterion 4 (Grammatical Accuracy): 🟢 YES or 🔴 NO

Notes: [Short observation or example per criterion, if applicable]

<|im_end|>
<|im_start|>assistant
"""
