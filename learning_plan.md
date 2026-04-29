# Your 6-Month Hands-On Rebuild Plan: SWE + ML/AI

**Time budget:** 1–2 focused hours/day, 6 days/week
**Learning style:** Hands-on, physical repetition, ADHD-friendly. Practice first, reference second.
**Goal:** Be able to sit down at a blank editor, with no AI assistance, and confidently build, debug, and explain real software and ML systems.
**Target roles:** Software Engineer / ML & AI Engineer
**Overarching project:** MTG Portfolio Tracker — evolves from a simple CLI tool into a deployed ML-powered card investment platform.

---

## The Core Philosophy

1. **No AI tools during practice.** No Copilot, no Claude, no ChatGPT autocomplete. Close the tab. This is the entire point.
2. **Practice first, reference second.** Attempt the exercise _first_, get stuck, and _then_ look up exactly what you need. Stuck for 20+ minutes? Look it up, then close the reference and do it again from memory.
3. **Type everything by hand.** No copy-paste, ever. Your fingers remember things your eyes don't.
4. **The 3x rule.** Every new concept gets built three times: once with help, once from memory the same day, once from memory the next day.
5. **Small daily reps beat marathons.** 90 minutes of typing every day beats 8 hours on Saturday.
6. **One rep = one win.** Solve one problem, build one feature, get one test passing. Stop. Commit it. That's a successful session.
7. **Movement is allowed and encouraged.** Stand up between problems. Pace while thinking. Your body wants to move while your brain works — let it.

---

## Daily Session Structure (90 minutes, ADHD-friendly)

| Time      | Activity                                                                        | Why                                             |
| --------- | ------------------------------------------------------------------------------- | ----------------------------------------------- |
| 0–5 min   | **Warmup typing drill.** Re-type yesterday's solution from scratch, no looking. | Physical recall, gets you into flow fast        |
| 5–35 min  | **Problem block 1.** Pick today's problem, attack it. Pomodoro-style.           | Fresh attention = hardest problem               |
| 35–40 min | **Move.** Stand up. Walk. Get water. Don't look at your phone.                  | Reset attention                                 |
| 40–70 min | **Problem block 2.** Either finish problem 1 or start a smaller second problem. | Second attention burst                          |
| 70–85 min | **Build block.** Add one tiny feature to the MTG Tracker.                       | Apply what you just learned to the real project |
| 85–90 min | **Commit.** git add, commit with a descriptive message, push.                   | Closes the loop, green square earned            |

---

## Tracking Progress (No Separate LOG.md)

Your commit messages _are_ your log. Write descriptive messages:

```
git commit -m "Add card search by name using Scryfall API, learned requests library"
git commit -m "Refactor collection to use Card class with __repr__, practiced dunder methods"
git commit -m "Implement price history tracking with deque, NeetCode stack problem clicked"
```

The green squares on your GitHub contribution graph plus meaningful commit messages tell the full story. No extra file to forget about.

**Weekly reflection (Sundays, 5 minutes):** Open your repo, run `git log --oneline` for the week, and ask yourself: what felt solid? What felt shaky? Adjust the next week. No written document required — just the mental check-in.

---

## The "Lookup, Don't Read" Resource Stack

- **[Python docs](https://docs.python.org/3/)** — official, searchable, the source of truth
- **[Scryfall API docs](https://scryfall.com/docs/api)** — the MTG data source, free, excellent documentation
- **[Real Python](https://realpython.com/)** — search "[topic] real python", their articles are scannable
- **[Stack Overflow](https://stackoverflow.com/)** — one specific question at a time, not browsing
- **[NeetCode YouTube](https://www.youtube.com/@NeetCode)** — short focused videos when you've already attempted a problem
- **[StatQuest](https://www.youtube.com/@statquest)** — for ML concepts, short videos that explain one thing well
- **[3Blue1Brown](https://www.youtube.com/@3blue1brown)** — only when you need math intuition

**The rule:** No resource is "assigned reading." Every resource is a tool you reach for when you're already mid-fight with a problem.

---

## Phase 1 — Python by Doing (Weeks 1–5)

**Goal:** Type Python in your sleep. Build the muscle memory of syntax, idioms, and standard library calls.

**Daily structure:**

- **Exercism Python exercises** ([exercism.org/tracks/python](https://exercism.org/tracks/python)). Solve, submit, read other people's solutions.
- **1 mini-build per session** — add a feature to the MTG Tracker.
- **End every session by re-typing one previous exercise from memory.** No looking.

**Concepts to hit, in order, but only via problems:**

- Week 1: variables, types, conditionals, loops → Exercism easy track
- Week 2: functions, lists, dicts → Exercism easy + medium
- Week 3: comprehensions, file I/O, exceptions → Exercism medium
- Week 4: classes, inheritance, dunder methods → Exercism medium
- Week 5: modules, virtualenvs, standard library tour → Exercism hard

**When stuck:** Check Python docs or Real Python _for the specific syntax you need_. 5 minutes max. Then close it and finish.

### MTG Tracker — Phase 1 Features (one per day)

Build these in order. Each one teaches a specific Python concept:

1. **Add a card by name, store in a list, print collection** — input(), lists, while loops
2. **Save collection to JSON file** — json module, file I/O, with statements
3. **Load collection from JSON on startup** — file reading, error handling (what if file doesn't exist?)
4. **Add quantity tracking** — dicts instead of plain strings
5. **Search your collection by card name** — string methods, loops, conditionals
6. **Delete a card by name** — list/dict manipulation, user input validation
7. **Pull card data from Scryfall API** — requests library, JSON parsing, API basics
8. **Display current price from Scryfall** — nested dict access, f-strings, formatting
9. **Show total portfolio value** — loops, arithmetic, accumulator pattern
10. **Add a Card class** — classes, **init**, **repr**, methods
11. **Refactor collection to use Card objects** — OOP, serialization (converting objects to/from JSON)
12. **Add error handling everywhere** — try/except, graceful failures, edge cases
13. **Add a menu system** — while loop + if/elif dispatch, clean user experience
14. **Color-code terminal output** — ANSI codes or colorama, making CLI tools feel polished

**The 3x rule applied:** Every Friday, delete the MTG Tracker and rebuild it from scratch. The first time it'll take 90 minutes. By week 5 it'll take 20.

**Exit test:** Open a blank file. In under 20 minutes, with no lookups, write a class that reads a JSON file, filters items by a condition, and writes results to a new file. If you can do this, move on.

---

## Phase 2 — Data Structures & Algorithms by Doing (Weeks 6–11)

**Daily structure:**

- **1 NeetCode problem per day**, following NeetCode's "Roadmap" order. Free at [neetcode.io/roadmap](https://neetcode.io/roadmap).
- **Attempt for 25 minutes before any hint.** If still stuck, watch _only_ the first 2 minutes of NeetCode's video, then close it and code it yourself.
- **The next day, re-solve yesterday's problem from scratch, no hints.**
- **Every Sunday, re-solve 3 problems from earlier in the week.**

**The order (NeetCode's roadmap):**

- Weeks 6–7: Arrays & Hashing → Two Pointers → Sliding Window
- Week 8: Stack → Binary Search
- Week 9: Linked List → Trees
- Week 10: Tries → Heap/Priority Queue → Backtracking
- Week 11: Graphs → Intro to DP

**When stuck conceptually:** [Visualgo](https://visualgo.net/) shows animations of every data structure. Watch the animation, close it, implement it yourself.

### MTG Tracker — Phase 2 Features

Each feature directly applies a data structure you're learning that week:

- **Fast card search with a hash map** — build your own hash-based lookup instead of looping through a list
- **Price history tracking with a deque** — store last N prices per card, implement as a circular buffer
- **Watchlist with a priority queue** — track cards you're watching, sorted by price change percentage. Implement the heap yourself.
- **"Similar cards" with a graph** — cards connected by shared tags (color, type, set). Build adjacency list, implement BFS to find cards N edges away
- **Binary search on sorted collection** — sort by price, implement binary search to find cards in a price range
- **Undo system with a stack** — track recent actions, let user undo them. Implement with your own stack.

**Exit test:** Given a brand-new NeetCode easy you've never seen, solve it in under 30 minutes, no hints. Then solve a brand-new medium in under 45.

---

## Phase 3 — ML by Building (Weeks 12–18)

**Daily structure:**

- **One Kaggle Learn micro-lesson per day** ([kaggle.com/learn](https://www.kaggle.com/learn)) — 10–15 min hands-on notebooks. Order: Pandas → Intro to ML → Intermediate ML → Feature Engineering → Intro to Deep Learning.
- **One ML algorithm from scratch per week** in pure NumPy: linear regression → logistic regression → k-NN → k-means → decision tree → tiny neural network.
- **Math via short videos, only when blocked.** StatQuest or 3Blue1Brown, 10 min max, then back to code.

**The "build it before you read about it" workflow:**

1. Day 1: Try to implement the algorithm from a one-paragraph description. Fail.
2. Day 2: Watch ONE StatQuest video (10 min). Try again. Get partway.
3. Day 3: Look up the math formula. Implement it. Get it working on tiny data.
4. Day 4: Test on bigger data. Compare to sklearn.
5. Day 5: Re-implement from scratch in one sitting, no notes.

**Math, the ADHD-friendly way:** No textbooks. 20 min/session, only when blocked:

- 3Blue1Brown's _Essence of Linear Algebra_ — watch one when you need it
- 3Blue1Brown's _Essence of Calculus_ — same
- StatQuest for stats and probability
- [Khan Academy practice exercises](https://www.khanacademy.org/math) — do the problems, don't watch videos

### MTG Tracker — Phase 3 Features (the ML layer)

This is where the project gets exciting. You're building a card investment intelligence tool:

- **Price trend analysis with Pandas** — pull historical price data, clean it, explore it, visualize trends
- **Linear regression on price trends** — predict where a card's price is heading. Build from scratch in NumPy first, then compare to sklearn.
- **Classification: will this card spike?** — logistic regression on card features (rarity, format legality, set age, color identity, EDHREC rank). Label cards that spiked >20% in the last month. Train a classifier to predict future spikes.
- **Random forest for price prediction** — use card metadata features. Compare your from-scratch decision tree to sklearn's random forest.
- **Clustering cards by price behavior** — k-means to find groups of cards that move together. Which clusters does your collection fall into?
- **Model evaluation dashboard** — accuracy, precision, recall, F1 on your spike predictor. Which cards is the model most confident about?

**Phase 3 project deliverable:** A Kaggle notebook showing your full pipeline — data collection from Scryfall, feature engineering, model training, evaluation, and a "top 10 cards likely to spike this month" prediction. Ship it public.

**Exit test:** On paper, no looking, write the formula for gradient descent and explain why it works. Then code logistic regression from scratch in under 45 minutes.

---

## Phase 4 — Deploy the MTG Tracker (Weeks 19–22)

Pure building. No "learning" — you learn by shipping.

### MTG Tracker — Phase 4: Full Stack Deployment

- **Week 19: FastAPI backend** — endpoints for: search cards, get portfolio, get price predictions, get watchlist alerts. Use [FastAPI's tutorial](https://fastapi.tiangolo.com/tutorial/) as a _lookup_ reference.
- **Week 20: Frontend** — minimal HTML/CSS/JS interface. Search cards, view your portfolio with current values, see buy/sell signals from your ML model. Keep it simple — function over beauty.
- **Week 21: Deploy** — put it live on Render or Railway (free tier). Write a README a human can actually read. Add screenshots.
- **Week 22: Polish and test** — add pytest tests, handle edge cases, clean up the code. Make sure a stranger could clone the repo and run it.

**ADHD survival tip:** Not "build the API" — instead "make a single endpoint that returns hello world." Then "make it return one card." Then "make it search." Each tiny win is dopamine. Stack them.

### Side project (1 week, fit it in):

The streak tracker you already started — polish it into a proper CLI tool with proper package structure and tests. Two portfolio pieces are better than one.

---

## Phase 5 — System Design & AI Engineering (Weeks 23–26)

**Daily structure:**

- **SQL:** [SQLZoo](https://sqlzoo.net/) or [PostgreSQL Exercises](https://pgexercises.com/) — 1 problem per day. SQL fluency alone will get you hired.
- **One "design this" per week** from the [System Design Primer](https://github.com/donnemartin/system-design-primer). Sketch on paper, then watch [ByteByteGo](https://www.youtube.com/@ByteByteGo) and compare.
- **Build one tiny version** of what you designed.

### MTG Tracker — Phase 5: AI-Powered Features

- **Move data to PostgreSQL** — migrate from JSON files to a real database. Write SQL queries for portfolio analytics.
- **Build a RAG system over MTG rules and card rulings** — chunk the Comprehensive Rules, embed them, store in ChromaDB, retrieve relevant rules when a user asks a question. Build the chunking and retrieval logic yourself before reaching for LangChain.
- **"Find similar cards" with embeddings** — embed card descriptions, find nearest neighbors for budget alternatives or deck-building suggestions.
- **Azure ML integration** — deploy your price prediction model to Azure ML (you already have the CLI set up). Serve predictions from the cloud.

**Additional resources:**

- [Hugging Face's NLP Course](https://huggingface.co/learn/nlp-course/chapter1/1) — interactive notebooks
- [Full Stack Deep Learning](https://fullstackdeeplearning.com/) — free, hands-on labs

---

## Phase 6 — Portfolio, Interview Prep, Job Hunt (Weeks 27+)

By now you have: a deployed ML-powered MTG Tracker, several Exercism solutions showing fundamentals, a streak tracker, and the ability to explain every line.

- **Polish the MTG Tracker:** clean README with screenshots, live demo link, architecture diagram, clear explanation of the ML models and why you chose them
- **Write 2–3 blog posts:** "How I built a price prediction model for Magic: The Gathering" is a post that gets clicks and shows real skill
- **Resume targeting both SWE and ML roles** — the MTG Tracker demonstrates both
- **Resume NeetCode/LeetCode** (1 problem/day, focus on patterns)
- **Mock interviews** with humans ([Pramp](https://www.pramp.com/) — free peer mock interviews)
- **Apply broadly, expect rejection, iterate**

---

## ADHD-Specific Survival Tactics

- **Body doubling.** [Focusmate](https://www.focusmate.com/) — free, silent co-working with a stranger. Rocket fuel for ADHD focus.
- **Pomodoro with a real timer.** Phone away. 25 on, 5 off.
- **Visible streaks.** GitHub contribution graph IS your streak tracker. Green squares = progress.
- **Stand and pace while thinking.** Sit only when typing.
- **The 2-minute start rule.** Commit to just 2 minutes. Type one line of code.
- **Music with no lyrics.** Lo-fi, video game soundtracks, brown noise.
- **Externalize your brain.** Sticky notes, whiteboards, paper.
- **One project at a time.** The MTG Tracker IS the project. Resist starting something else.
- **Bad days are part of the plan.** Do 20 minutes of typing drills and call it a win. Streaks > intensity.

---

## Anti-Overwhelm Rules

- **If you miss a day, you do not "make it up."** Resume the next day.
- **If you finish a phase early, do not skip ahead.** Add another feature to the MTG Tracker. Mastery > speed.
- **If you finish a phase late, that's fine.** Not a race.
- **One day a week is rest.** No code, no guilt.
- **Once a month, honest review.** What feels solid? What feels shaky? Adjust.

---

## On AI Tools (the hard part)

- **Months 1–4:** Zero AI tools while learning. Period. Uninstall Copilot. This is detox.
- **Months 5–6:** Use AI to _review_ code you've already written and working. Ask "what would you do differently?" Evaluate critically.
- **After the plan:** AI as a senior pair programmer, not a crutch. Test: if your AI tools disappeared tomorrow, could you still do your job?

---

## Your Tools

- **Editor:** Neovim (your config, your keybindings — it's yours)
- **Terminal:** iTerm2 with split panes
- **Version control:** Git + GitHub (public repos, daily commits)
- **Notebooks:** Jupyter Lab in browser for lab work, jupytext for conversion
- **Cloud:** Azure CLI for ML deployment in Phase 5
- **API:** Scryfall (free, no auth required) for all MTG data

---

## Right Now

```bash
mkdir -p projects/mtg-tracker
nvim projects/mtg-tracker/mtg_tracker.py
```

Version one: add a card by name, list your collection, save to JSON. You already know every skill this requires. Go build it.
