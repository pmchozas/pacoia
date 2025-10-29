
prompt = \
"""
<|im_start|>system
You are an evaluation assistant. Your task is to assess the **organization** of the speech or presentation transcript based on the given criteria. Follow the criteria carefully and answer with 🟢 YES or 🔴 NO for each. Provide brief justifications where applicable.
<|im_end|>
<|im_start|>user
# Evaluation Task

Grade the **organization of the text** according to the following criteria:

---

## Criterion 1: Use of Connecting Devices and Signposts

> Does the speech contain **at least 5 connecting devices or signposts**?

### Look for:
- Examples of signposts: "Firstly", "In addition", "To conclude", "On the other hand", etc.
- Look for natural transitions or logical connections between ideas or sections.

(e.g. "Building on that idea..." "Another key aspect to consider is..." "Moving on to another important point..." "Additionally, it's important to note that..."
"A further example of this is..." "To illustrate this point further..." "Another argument in favour of this is..." "For instance, let's take a look at..."
To link a new idea to the previous one
"This leads us to the next point..." "Following on from this..." "As a result of this..." "This is closely connected to..." "An extension of this idea is..."
To introduce a contrasting view
"However, there is another perspective to consider..." "On the other hand..." "In contrast to this..." "Despite this, some argue that..." "Alternatively, we could look at it from another angle..."
"This brings us to the end of this section..."
"With that, we conclude this part of the discussion..."
"That wraps up our discussion on..."
"Having explored this, we can now move on to..."
"This concludes our analysis of..."
"Thank you for your attention, and I welcome any questions you may have."
"That concludes my presentation, thank you."
"I appreciate your time, and I'm happy to address any questions."
"With that, I conclude my talk, and I'd be glad to hear your thoughts.")

**Answer with:** 🟢 YES or 🔴 NO

---

## Criterion 2: Closing Summary or Mention of Objectives

> Does the speech **close with a summary of the contribution** or a mention of the objectives of the proposal?

### Look for:
- A final statement summarizing the key points or contributions of the presentation.
- A mention of goals or objectives of the proposal in the conclusion.

**Answer with:** 🟢 YES or 🔴 NO

---

## Criterion 3: Invitation to Ask Questions

> Does the speech contain an **invitation to ask questions** at the end?

### Look for:
- Common phrases like "Thank you very much for listening, we are pleased to answer any questions you may have."
- Any formal or polite invitation to engage with the audience at the end.

**Answer with:** 🟢 YES or 🔴 NO

---

## Criterion 4: Emphasis

> Does the speech show **emphasis**?

### Look for:
- Repetitions of words
- The use of adjectives
- The use of common phrasing such as "As we have explained", "The most important idea is", "This is important because"

**Answer with:** 🟢 YES or 🔴 NO

---

## Criterion 5: Visual Aids

> Does the speech contain **mentions to visual aids**?

### Look for:
- Expressions such as "As shown in the previous slide"
- Expressions such as "As shown in the diagram"
- Expressions such as "As shown in the figure"

**Answer with:** 🟢 YES or 🔴 NO
---

## Criterion 6: Parallel structures

> Does the speech respect **parallel structures**  in an enumeration or listing?

### Look for:
- The same structure in enumerations, for examle: "First, we explain the idea. Second, we describe the problem. Third, we find a solution."

**Answer with:** 🟢 YES or 🔴 NO

---

## Criterion 7: Closing

> Does the speech conclude with a proper **closing**?

### Look for:
- Mentions to a brief summary of the speech
- Mentions to a brief summary of the problems and the contribution to solve them
- If applicable, an answer to a question previously mentioned in the speech

**Answer with:** 🟢 YES or 🔴 NO

---

## Transcription Input

{}

---

## Expected Output Format

Criterion 1 (Connecting Devices and Signposts): 🟢 YES or 🔴 NO
Criterion 2 (Closing Summary or Objectives): 🟢 YES or 🔴 NO
Criterion 3 (Invitation to Ask Questions): 🟢 YES or 🔴 NO
Criterion 4 (Emphasis): 🟢 YES or 🔴 NO
Criterion 5 (Visual Aids): 🟢 YES or 🔴 NO
Criterion 6 (Parallel Structures): 🟢 YES or 🔴 NO
Criterion 7 (Closing): 🟢 YES or 🔴 NO

Notes: [Short observation or example per criterion, if applicable]

<|im_end|>
<|im_start|>assistant
"""
