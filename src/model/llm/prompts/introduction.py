
prompt = \
"""
<|im_start|>system
You are an expert evaluator of presentation introductions. Your job is to assess whether the introduction meets specific rhetorical and structural criteria. Your evaluation must strictly follow the guidelines and format described below.
<|im_end|>
<|im_start|>user
# Task

Grade the **introduction** of a presentation based on the following three criteria. Respond only with **YES or 🔴 NO**, and provide brief supporting notes.

---

## Criterion 1: Attention-Grabbing Sentence

> Does the speech begin with a specific sentence that intends to grab the audience's attention?

**Answer with:** 🟢 YES or 🔴 NO

### Examples of Attention-Grabbers:

- ** A statistic:**
  _Example:_ “Did you know that 80% of the items we own are never used?”

- ** A personal reference, story, or anecdote:**
  _Example:_ “When I was a kid, I always wanted to have a slide.”

- ** A rhetorical or open question:**
  _Example:_ “What if we just stop wearing socks?”

- ** A joke:**
  _Example:_ “I was going to tell a time-traveling joke during my speech, but you didn't like it.”

- **A shocking statement or startling statistic**
  _Example:_ "Every year, over 8 million tons of plastic end up in our oceans — that's the equivalent of dumping a garbage truck full of plastic into the sea every single minute."

- **A quotation by an expert or well-known person**
  _Example:_ “As Albert Einstein once said: “We cannot solve our problems with the same thinking we used when we created them.”

- **A rhetorical or open-ended question that generates discussion from the audience**
  _Example:_ "What would your life look like if you had no access to the internet for just one week?"

- **An appropriate joke or humor**
  _Example:_ "They say money can't buy happiness — but it can buy coffee, and that's pretty close!"

- **A demonstration or dramatic presentation aid**
  _Example:_ "This is the water most of us drink every day… and this is the water that millions of people around the world have no choice but to drink."

- **A related story or anecdote**
  _Example:_ "When I was in college, I missed an important class because I relied on a friend to wake me up. That one missed class eventually cost me a whole grade — and it taught me never to outsource responsibility for my own growth."

- **A personal reference, compliment to the audience, or a reference to the occasion of the presentation**
  _Example:_ "It's an honor to be here today speaking to such a dedicated group of professionals. I know many of you traveled long distances to attend this conference, and that kind of commitment tells me this is a room full of people who truly care about making a difference."

---

## Criterion 2: Clear Topic Introduction

> Does the speech set the theme or introduce the topic clearly within the first paragraph?

**Answer with:** 🟢 YES or 🔴 NO

### Observations:

- The speaker usually refers to an algorithm, product, system, website, or service.
- The topic is often related to **AI** or a named application/platform.

---

## Criterion 3: Structural Outline

> Does the introduction describe the outline of the presentation?

**Answer with:** 🟢 YES or 🔴 NO

### Observations:

- The speaker must mention future sections, such as:
  - **State of the Art** (also: Background, Literature Review, or Related Work)
  - **Innovation**
  - **Description** or **Methodology**

---

## Transcription Input

{}

---

## Expected Output

Please return your evaluation in the following format:

Criterion 1 (Attention Grabber): 🟢 YES or 🔴 NO
Criterion 2 (Topic Introduction): 🟢 YES or 🔴 NO
Criterion 3 (Structural Outline): 🟢 YES or 🔴 NO

Notes: [Brief explanation per criterion]

<|im_end|>
<|im_start|>assistant
"""
