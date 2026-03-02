# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

1. If you guess a number not within 1 and 100, it would not tell you that it was a valid guess.
2. The number that I got was 38, and the game kept telling me to go higher even after guessing 100.
3. The game gives you 7 attempts however, I only submitted 6 guesses.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

1. I used Copilot
2. An AI Suggestion that was correct was fixing the guess checker. The bug was telling me that my guess was always higher, now it correctly can pinpoint me to where the secret number is whether it is higher or lower or on the dot.
3. An AI Suggestion that I got incorrect was trying to fix the amount of attempts I had. It seems like it increased it to 8 by mistake and I told it to fix that mistake, to be back to 7.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

1. I used random test cases to ensure that each bug was fixed, such as trial running a bunch of numbers to ensure the amount of attempts was counted corrctly and also guessing numbers to see if the guess checker was directing me correctly to the secret number.
2. One test I ran, I just counted up from 1 to 10 to see if in normal mode, that I am only allotted 7 turns. The first trial run, it let me have 8 attempts, which I had to fix back to 7 attempts.
3. Ai did help me design and understand these tests, such that I was looking for the exact variable that defined the amount of turns that I was allotted, and now it can be simply changed in the code.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

1. In this line: st.session_state.secret = random.randint(low, high), we get a random integer in every session of the game depending on what the low and high number is.
2. Reruns would be similar to someone erasing their drawing and redrawing it from the top so that there is a new and clean picture of what your looking at. Session state is like a save file, so that if we were to save our session in a middle of a pokemon game, your progress is saved, and in our game the session state saves our score.
3. We actually had to save the secret number to a session state so that the number would not be lost.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

1. One strategy I would reuse would be to make variables more clearly defined, such as looking for where the secret variable was, the allotted turns, and also the score.
2. One thing I would do differently with AI is I would be less reliant on Copilot. I fel like the allotted attempts felt like a very simple fix if it was more defined clearer in the code.
3. I feel like this project gave me a good idea of how AI generated code would work for Copilot especially just being more specific with problems using different sessions. I feel like that was a really useful tool just to help AI not get confused with different problems.
