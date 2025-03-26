## Metrics

### Deepseek-r1:8b  

#### Cohesion Index
- Formula: (total number of words - average word length) / total number of words * 100
- Result: ((114-5.5)/114)*100 ≈ 95.1%

#### Reasoning Score
- Formula: (number of explicit references to literature or evidence + number of explicit reasoning processes) / total number of sentences * 100
- Result: (0 +1)/9*100 ≈ 11%

#### Content metric
- Formula: NA
- Result: NA

### Llama3.1:8b

#### Cohesion Index
- Formula: CI = (Number of Cohesive Devices / Total Number of Words) x 100
- Result: CI = (3 / 126) x 100 ≈ 2.38

#### Reasoning Score
- Formula: RS = (Number of Abstract Concepts + Number of Evaluative Language) / Total Number of Words
- Result: RS = (3 + 2) / 126 ≈ 0.0476

#### Argumentative Density
- Formula: AD = (Number of Claims + Number of Evidence) / Total Number of Words
- Result: AD = (2 + 1) / 126 ≈ 0.0159

#### Content
- Formula: C = (Number of Accurate Information + Number of Relevant Sources) / Total Number of Words
- Result: C = (3 / 126) ≈ 0.0238
  
#### Conclusion
- Formula: C = (Number of Effective Summary + Number of Relating to Introduction) / Total Number of Words
- Result: C = (1 / 126) ≈ 0.0079

#### Vocal Delivery
- Formula: VD = (Number of Clear Transitions + Number of Effective Use of Rhetorical Devices) / Total Number of Words
- Result: VD = (3 / 126) ≈ 0.0238, adjusted for fillers and hesitations: VD ≈ 0

#### Language
- Formula: L = (Number of Formal Vocabulary + Number of Correct Grammar) / Total Number of Words
- Result: L ≈ (2 / 126) = 0.0159

### Mistral:7b

NA

### o4

#### Cohesion Index
- Formula: Cohesion Index = Number of cohesive devices / Total number of sentences
- Result: Cohesion Index = 4 / 7 = 0.57

#### Reasoning Score
- Formula: Reasoning Score = (Number of reasoned arguments / Total number of arguments) × 100
- Result: Reasoning Score = (2 / 3) × 100 = 66.67

#### Argumentative Density
- Formula: Argumentative Density = Number of arguments / Total number of words
- Result: Argumentative Density = 3 / 55 = 0.055

#### Formality Index Calculation  
- Formula: Formality Index = (Formal words - Informal words) / Total words
- Result: Formality Index = (4 - 2) / 55 = 0.036 (3.6%)
  
#### Hedging Evaluation 
- Formula: Hedging Evaluation = Number of hedging expressions / Total number of sentences
- Result: Hedging Evaluation = 1 / 7 = 0.14

#### Type-Token Ratio Calculation 
- Formula: Type-Token Ratio = (Unique words / Total words) × 100
- Result: Type-Token Ratio = (41 / 55) × 100 = 74.55

### Qwen2.5:7b

#### Cohesion Index
- Formula: Cohesion Index = (Number of cohesive elements) / (Total number of clauses)
- Result: Cohesion Index = 6 / 8 = 0.75

#### Reasoning Score
- Formula: Reasoning Score = (Number of logical transitions) / (Total number of sentences)
- Result: Reasoning Score = 4 / 8 = 0.5

#### Argumentative Density
- Formula: Argumentative Density = (Number of argumentative statements) / (Total number of clauses)
- Result: Argumentative Density = 3 / 8 = 0.375

## Metrics Comparison

## Evaluation 

### Deepseek-r1:8b  

| **Category**      | **Criteria**                                            | **Grade** |
|------------------|--------------------------------------------------------|----------|
| **Cohesion Index**| High connectivity with clear transitions             | **1**    |
| **Reasoning Score**| Minimal evidence-based reasoning                     | **0.5**  |
| **Content**       | Relevant but lacks depth in research and metaphor     | **0.5**  |
| **Organization** | Lacks explicit signposting but logical flow          | **0.5**  |
| **Vocal Delivery**| Generally fluent with minimal hesitations            | **1**    |
| **Language Use**  | Formal, clear without slang or errors               | **0.5**  |
| **Conclusion**   | Summarizes well and relates to introduction             | **0.5**  |

### Llama3.1:8b  

| **Category**      | **Criteria**                                            | **Grade** |
|------------------|--------------------------------------------------------|----------|
| **Introduction** | Well-integrated attention-getting technique or opener  | **1**    |
|                 | Sets the theme or introduces the topic clearly          | **1**    |
|                 | Shows the outline of the presentation appropriately     | **0.5**  |
| **Organization** | Opens and closes each section with clear transitions   | **0.5**    |
|                 | Has a logical progression of ideas                      | **1**    |
|                 | Balances parts in terms of length and content           | **0.5**  |
| **Content**      | Adapts the content to the audience                     | **1**    |
|                 | Shows evidence of literature research                   | **0**    |
|                 | Includes a visual metaphor or simile                    | **0.5**    |
| **Conclusion**   | Summarizes main points effectively                     | **0.5**  |
|                 | Relates to the introduction                             | **0.5**  |
|                 | Invites questions effectively                           | **0.5**  |
| **Vocal Delivery** | Fluency (avoiding hesitations and fillers)           | **0**    |
| **Language**     | Employs characteristics of spoken formal language      | **0**  |
|                 | Uses topically rich and diverse vocabulary              | **NA**    |
|                 | Uses grammar correctly                                  | **0**    |

### Mistral:7b

| **Category**      | **Criteria**                                            | **Grade** |
|------------------|--------------------------------------------------------|----------|
| **Introduction** | Well-integrated attention-getting technique or opener  | **1**    |
|                 | Sets the theme or introduces the topic clearly          | **1**    |
|                 | Shows the outline of the presentation appropriately     | **0.5**  |
| **Organization** | Opens and closes each section with clear transitions   | **0**    |
|                 | Has a logical progression of ideas                      | **1**    |
|                 | Balances parts in terms of length and content           | **0.5**  |
| **Content**      | Adapts the content to the audience                     | **NA**    |
|                 | Shows evidence of literature research                   | **NA**    |
|                 | Includes a visual metaphor or simile                    | **NA**    |
| **Conclusion**   | Summarizes main points effectively                     | **0.5**  |
|                 | Relates to the introduction                             | **0.5**  |
|                 | Invites questions effectively                           | **0.5**  |
| **Vocal Delivery** | Fluency (avoiding hesitations and fillers)           | **NA**    |
| **Language**     | Employs characteristics of spoken formal language      | **NA**  |
|                 | Uses topically rich and diverse vocabulary              | **NA**    |
|                 | Uses grammar correctly                                  | **NA**    |

### o4

| **Category**      | **Criteria**                                            | **Grade** |
|------------------|--------------------------------------------------------|----------|
| **Introduction** | Well-integrated attention-getting technique or opener  | **1**    |
|                 | Sets the theme or introduces the topic clearly          | **1**    |
|                 | Shows the outline of the presentation appropriately     | **0.5**  |
| **Organization** | Opens and closes each section with clear transitions   | **1**    |
|                 | Has a logical progression of ideas                      | **1**    |
|                 | Balances parts in terms of length and content           | **0.5**  |
| **Content**      | Adapts the content to the audience                     | **1**    |
|                 | Shows evidence of literature research                   | **0**    |
|                 | Includes a visual metaphor or simile                    | **0**    |
| **Conclusion**   | Summarizes main points effectively                     | **0.5**  |
|                 | Relates to the introduction                             | **0.5**  |
|                 | Invites questions effectively                           | **0.5**  |
| **Vocal Delivery** | Fluency (avoiding hesitations and fillers)           | **0**    |
| **Language**     | Employs characteristics of spoken formal language      | **0.5**  |
|                 | Uses topically rich and diverse vocabulary              | **1**    |
|                 | Uses grammar correctly                                  | **1**    |

### Qwen2.5:7b

| **Category**      | **Criteria**                                            | **Grade** |
|------------------|--------------------------------------------------------|----------|
| **Introduction** | Well-integrated attention-getting technique or opener  | **1**    |
|                 | Sets the theme or introduces the topic clearly          | **1**    |
|                 | Shows the outline of the presentation appropriately     | **0.5**  |
| **Organization** | Opens and closes each section with clear transitions   | **0.5**  |
|                 | Has a logical progression of ideas                      | **1**    |
|                 | Balances parts in terms of length and content           | **0.5**  |
| **Content**      | Adapts the content to the audience                     | **1**    |
|                 | Shows evidence of literature research (oral citations or references)  (0)|
|                 | Includes a visual metaphor or simile to clarify an idea (0.5) |
| **Conclusion**   | Summarizes main points effectively                      | **0.5**  |
|                 | Relates to the introduction                            | **0.5**  |
|                 | Invites questions effectively                          | **0.5**  |
| **Vocal Delivery**| Fluent, avoiding frequent repetitions, hesitations and gap fillers (0)|
| **Language**     | Employs characteristics of spoken formal language      | **0.5**  |
|                 | Uses topically rich and diverse vocabulary              | **1**    |
|                 | Uses grammar correctly                                 | **1**    |

## Evaluation Comparison

| **Category**      | **Criteria**                                          | **o4**   | **Qwen2.5:7b** | **Mistral:7b** | **Llama3.1.:8b** | **Deepseek-r1:8b** |
|------------------|--------------------------------------------------------|----------|----------------|----------------|------------------|--------------------|
| **Introduction** | Well-integrated attention-getting technique or opener  | **1**    | **1**          | **1**          | **1**            | **NA**             |
|                  | Sets the theme or introduces the topic clearly         | **1**    | **1**          | **1**          | **1**            | **NA**             |
|                  | Shows the outline of the presentation appropriately    | **0.5**  | **0.5**        | **0.5**        | **0.5**          | **NA**             |
| **Organization** | Opens and closes each section with clear transitions   | **1**    | **0.5**        | **0**          | **0.5**          | **NA**             |
|                  | Has a logical progression of ideas                     | **1**    | **1**          | **1**          | **1**            | **NA**             |
|                  | Balances parts in terms of length and content          | **0.5**  | **0.5**        | **0.5**        | **0.5**          | **NA**             |
| **Content**      | Adapts the content to the audience                     | **1**    | **1**          | **NA**         | **1**            | **NA**             |
|                  | Shows evidence of literature research                  | **0**    | **0**          | **NA**         | **0**            | **NA**             |
|                  | Includes a visual metaphor or simile                   | **0**    | **0.5**        | **NA**         | **0.5**          | **NA**             |
| **Conclusion**   | Summarizes main points effectively                     | **0.5**  | **0.5**        | **0.5**        | **0.5**          | **NA**             |
|                  | Relates to the introduction                            | **0.5**  | **0.5**        | **0.5**        | **0.5**          | **NA**             |
|                  | Invites questions effectively                          | **0.5**  | **0.5**        | **0.5**        | **0.5**          | **NA**             |
| **Vocal Delivery** | Fluency (avoiding hesitations and fillers)           | **0**    | **0**          | **NA**         | **0**            | **NA**             |
| **Language**     | Employs characteristics of spoken formal language      | **0.5**  | **0.5**        | **NA**         | **0**            | **NA**             |
|                  | Uses topically rich and diverse vocabulary             | **1**    | **1**          | **NA**         | **NA**           | **NA**             |
|                  | Uses grammar correctly                                 | **1**    | **1**          | **NA**         | **0**            | **NA**             |