# Your 6-Month Hands-On Rebuild Plan: SWE + ML/AI

**Time budget:** 1–2 focused hours/day, 6 days/week
**Learning style:** Hands-on, physical repetition, ADHD-friendly. Practice first, reference second.
**Goal:** Be able to sit down at a blank editor, with no AI assistance, and confidently build, debug, and explain real software and ML systems.
**Target roles:** Software Engineer / ML & AI Engineer

---

## The Core Philosophy (read this once, then never again — it's the only "reading" required)

1. **No AI tools during practice.** No Copilot, no Claude, no ChatGPT autocomplete. Close the tab. This is the entire point.
2. **Practice first, reference second.** You don't read a chapter then do exercises. You attempt the exercise *first*, get stuck, and *then* look up exactly what you need. Stuck for 20+ minutes? Look it up, then close the reference and do it again from memory.
3. **Type everything by hand.** No copy-paste, ever. Your fingers remember things your eyes don't.
4. **The 3x rule.** Every new concept gets built three times: once with help, once from memory the same day, once from memory the next day. This is the physical repetition your brain needs.
5. **Small daily reps beat marathons.** 90 minutes of typing every day beats 8 hours on Saturday. Your brain consolidates between sessions, especially with ADHD.
6. **One rep = one win.** Solve one problem, build one feature, get one test passing. Stop. Log it. That's a successful session.
7. **Movement is allowed and encouraged.** Stand up between problems. Pace while thinking. Whiteboard on a wall. Your body wants to move while your brain works — let it.

---

## Daily Session Structure (90 minutes, ADHD-friendly)

This is built in short blocks because your attention will fade — and that's fine, it's how your brain works.

| Time | Activity | Why |
|---|---|---|
| 0–5 min | **Warmup typing drill.** Re-type yesterday's solution from scratch, no looking. | Physical recall, gets you into flow fast |
| 5–35 min | **Problem block 1.** Pick today's problem, attack it. Pomodoro-style. | Fresh attention = hardest problem |
| 35–40 min | **Move.** Stand up. Walk. Get water. Don't look at your phone. | Reset attention |
| 40–70 min | **Problem block 2.** Either finish problem 1 or start a smaller second problem. | Second attention burst |
| 70–85 min | **Build block.** Add one tiny thing to your current project. | Apply what you just learned |
| 85–90 min | **Log win.** Write down: what you built, what stuck, what to redo tomorrow. | Closes the loop, shows progress |

Some days you'll hyperfocus and want to keep going. Let yourself, but **stop at 2 hours max** — anything beyond that wrecks tomorrow's session. ADHD hyperfocus borrows energy from the future; don't overdraft.

Some days you'll have nothing. Do 30 minutes of pure typing drills (re-type a solution from a previous day) and call it a win. Streaks matter more than length.

---

## The "Lookup, Don't Read" Resource Stack

You don't sit down and read these. You attack a problem first, hit a wall, *then* search these for the specific thing you need. 5–10 minutes max per lookup. Then close the tab and try again.

- **[Python docs](https://docs.python.org/3/)** — official, searchable, the source of truth
- **[Real Python](https://realpython.com/)** — search "[topic] real python", their articles are scannable
- **[Stack Overflow](https://stackoverflow.com/)** — you're allowed to use it for *one specific question at a time*, not browsing
- **[NeetCode YouTube](https://www.youtube.com/@NeetCode)** — short focused videos when you've already attempted a problem
- **[StatQuest](https://www.youtube.com/@statquest)** — for ML concepts, short videos that explain one thing well
- **[3Blue1Brown](https://www.youtube.com/@3blue1brown)** — only when you need math intuition. Visual, brain-friendly, never longer than 20 min

**The rule:** No resource is "assigned reading." Every resource is a tool you reach for when you're already mid-fight with a problem.

---

## Phase 1 — Python by Doing (Weeks 1–5)

**Goal:** Type Python in your sleep. Build the muscle memory of syntax, idioms, and standard library calls.

**Daily structure:**
- **3 Exercism Python exercises per day** ([exercism.org/tracks/python](https://exercism.org/tracks/python)). Free, hands-on, no reading. Solve, submit, then look at other people's solutions to learn alternatives. This is your spine.
- **1 mini-build per session** — add a feature to the Phase 1 project (below).
- **End every session by re-typing one previous exercise from memory.** No looking.

**Concepts to hit, in order, but only via problems:**
- Week 1: variables, types, conditionals, loops → Exercism easy track
- Week 2: functions, lists, dicts → Exercism easy + medium
- Week 3: comprehensions, file I/O, exceptions → Exercism medium
- Week 4: classes, inheritance, dunder methods → Exercism medium
- Week 5: modules, virtualenvs, standard library tour → Exercism hard

**When stuck:** Check Python docs or Real Python *for the specific syntax you need*. 5 minutes max. Then close it and finish.

**Phase 1 project (build a little every day):** A command-line task tracker. Start with: "add a task, print all tasks." That's it for day 1. Each day after, add ONE thing: complete tasks, delete, save to file, load from file, dates, priorities, search, tags, classes, error handling. By week 5 you have a real CLI app you built one feature at a time, the ADHD-friendly way.

**The 3x rule applied:** Every Friday, delete your task tracker and rebuild the whole thing from scratch in one session. Yes, the whole thing. The first time it'll take 90 minutes. By week 5 it'll take 20.

**Exit test:** Open a blank file. In under 20 minutes, with no lookups, write a class that reads a CSV file, filters rows by a condition, and writes the filtered rows to a new file. If you can do this, move on. If not, do one more week of Exercism medium problems.

---

## Phase 2 — Data Structures & Algorithms by Doing (Weeks 6–11)

This is the phase you'll like most. It's *all* problem-solving. Almost no reading.

**Daily structure:**
- **1 NeetCode problem per day**, following NeetCode's "Roadmap" order (it's organized by pattern). Free at [neetcode.io/roadmap](https://neetcode.io/roadmap).
- **Attempt for 25 minutes before any hint.** If still stuck, watch *only* the first 2 minutes of NeetCode's video (the explanation of the approach), then close the video and code it yourself.
- **The next day, re-solve yesterday's problem from scratch, no hints.** This is the physical repetition. If you can't, do it again the day after too.
- **Every Sunday, re-solve 3 problems from earlier in the week.** Same rule: from scratch, no hints.

**The order (NeetCode's roadmap):**
- Weeks 6–7: Arrays & Hashing → Two Pointers → Sliding Window
- Week 8: Stack → Binary Search
- Week 9: Linked List → Trees (this is where it gets fun)
- Week 10: Tries → Heap/Priority Queue → Backtracking
- Week 11: Graphs → Intro to DP

**The drill that builds real fluency:** Pick 5 problems you've already solved. Set a timer. Solve all 5 from scratch in one session. This is the equivalent of a musician running scales — boring at first, then suddenly your hands just know the patterns.

**When stuck conceptually:** [Visualgo](https://visualgo.net/) shows animations of every data structure. Watch the animation, close it, implement the structure yourself.

**Phase 2 project:** Take your task tracker. Add: keyword search (you'll use a hashmap), priority queue for due dates (you'll implement a heap), tag relationships (you'll build a small graph). Each feature is built by *you*, not imported from a library.

**Exit test:** Given a brand-new NeetCode easy you've never seen, solve it in under 30 minutes, no hints. Then solve a brand-new medium in under 45.

---

## Phase 3 — ML by Building (Weeks 12–18)

This is the phase where most people get lost in math books. You won't, because you're going to *build* every concept before you study it.

**Daily structure:**
- **One Kaggle Learn micro-lesson per day** ([kaggle.com/learn](https://www.kaggle.com/learn)) — they're 10–15 min hands-on notebooks, perfect ADHD format. Order: Python → Pandas → Intro to ML → Intermediate ML → Feature Engineering → Intro to Deep Learning.
- **One implementation from scratch per week.** Pick one algorithm and code it in pure NumPy with no sklearn. Linear regression. Then logistic regression. Then k-NN. Then k-means. Then a decision tree. Then a tiny neural network. Six algorithms, six weeks. Each one teaches you more than reading 10 books.
- **Math via short videos, only when you need them.** Hit a concept you don't get? Search StatQuest or 3Blue1Brown for that specific thing. 10 min max. Then go back to the code.

**The "build it before you read about it" workflow for each algorithm:**
1. Day 1: Try to implement it from a one-paragraph description. Fail.
2. Day 2: Watch ONE StatQuest video on it (10 min). Try again. Get partway.
3. Day 3: Look up the math formula. Implement it. Get it working on a tiny dataset.
4. Day 4: Test it on a slightly bigger dataset. Compare to sklearn's version.
5. Day 5: Re-implement from scratch in one sitting, no notes. This is the win.

**Math, the ADHD-friendly way:** No textbooks. 20 minutes per session, only when a concept blocks you:
- 3Blue1Brown's *Essence of Linear Algebra* — 15 short videos, watch one when you need it
- 3Blue1Brown's *Essence of Calculus* — same deal
- StatQuest for stats and probability — search the specific concept
- [Khan Academy practice exercises](https://www.khanacademy.org/math) — actually do the problems, don't watch the videos

**Phase 3 project:** Pick a Kaggle dataset that interests you (something you actually care about — sports, music, games, whatever). Build the entire pipeline: load, clean, explore, engineer features, train three models (two of yours-from-scratch, one sklearn), evaluate properly, write a half-page explanation of what you found. Ship it as a Kaggle notebook so it's public.

**Exit test:** On paper, no looking, write the formula for gradient descent and explain in your own spoken words why it works. Then code logistic regression from scratch in under 45 minutes.

---

## Phase 4 — End-to-End Projects (Weeks 19–22)

Pure building. No "learning" in this phase — you learn by shipping.

**Project A — A real ML web app (3 weeks):**
Pick something you'd actually use. A predictor for a hobby, a classifier for something you care about. Build it end-to-end:
- Train and save a model (week 1)
- Build a FastAPI backend that serves predictions (week 2) — use [FastAPI's tutorial](https://fastapi.tiangolo.com/tutorial/) as a *lookup* reference
- Build a minimal HTML/CSS/JS frontend (week 3)
- Deploy it free on Render or Railway
- Write a README a human can actually read

**Project B — A useful CLI tool (1 week):**
A file organizer, a study timer, a personal expense tracker. Something you'll actually use yourself. Proper package structure. Tests with pytest (you'll learn pytest by *using* it, not reading about it).

**The rule:** Every line is yours. When stuck, you read docs, you experiment in a REPL, you try things. You do not ask AI. The struggle is the curriculum.

**ADHD survival tip for projects:** Break every feature into its smallest possible piece. Not "build the API" — instead "make a single endpoint that returns hello world." Then "make it accept a parameter." Then "make it call the model." Each tiny win is dopamine. Stack the tiny wins.

---

## Phase 5 — System Design & AI Engineering (Weeks 23–26)

System design is the hardest thing to learn hands-on, but we'll try.

**Daily structure:**
- **SQL is non-negotiable.** Do [SQLZoo](https://sqlzoo.net/) or [PostgreSQL Exercises](https://pgexercises.com/) — both are pure problem-solving sites, no reading. 1 problem per day for the whole phase. SQL fluency alone will get you hired.
- **One "design this" exercise per week.** Pick a system from the [System Design Primer](https://github.com/donnemartin/system-design-primer) (free GitHub repo). Sketch the architecture on paper. Then watch the corresponding [ByteByteGo YouTube video](https://www.youtube.com/@ByteByteGo) and compare. Short videos, very visual, ADHD-friendly.
- **Build one tiny version of the system you designed.** A URL shortener with Flask + SQLite. A toy chat app. A toy news feed. Tiny, ugly, works.

**AI engineering hands-on:**
- **Build a RAG system from scratch** (week 25–26). Pick something you know — your bootcamp notes, a book, something from a topic you love. Chunk it yourself. Embed it with a free model. Store it in [ChromaDB](https://www.trychroma.com/) (free, local). Retrieve. Pass to an LLM via API. Get answers with citations. Build the chunking and retrieval logic *yourself* before reaching for LangChain.
- **[Hugging Face's NLP Course](https://huggingface.co/learn/nlp-course/chapter1/1)** — interactive notebooks, not a textbook. Do them as exercises.
- **[Full Stack Deep Learning](https://fullstackdeeplearning.com/)** — free, all the labs are hands-on Jupyter notebooks.

---

## Phase 6 — Portfolio, Interview Prep, Job Hunt (Weeks 27+)

By now you have: 4–5 real projects on GitHub, the ability to explain every line, and the muscle of solving problems without crutches.

- Polish the three best projects: clean READMEs, screenshots, live demos
- Write 2–3 short blog posts on things you learned. Teaching is the final test.
- Resume targeting both SWE and ML roles
- Resume LeetCode (1 problem/day, focus on patterns you know)
- Mock interviews with humans (try [Pramp](https://www.pramp.com/) — free peer mock interviews)
- Apply broadly, expect rejection, iterate

---

## ADHD-Specific Survival Tactics

These matter as much as the curriculum.

- **Body doubling.** Code on Zoom with a friend (silently, both working) or use a free body-doubling app like [Focusmate](https://www.focusmate.com/). Having another human present is rocket fuel for ADHD focus.
- **Pomodoro with a real timer.** Phone away. A physical kitchen timer is best. 25 on, 5 off.
- **Visible streaks.** A wall calendar. A big X on every day you did your session. Don't break the chain. The visual cue matters more than you'd think.
- **Stand and pace while thinking.** Sit only when typing. Some of your best problem-solving will happen on your feet.
- **The 2-minute start rule.** If you don't want to start, commit to just 2 minutes. Type one line of code. The hardest part is starting, not continuing.
- **Music with no lyrics.** Lo-fi, video game soundtracks, brown noise. Whatever blocks the world out without competing for the language part of your brain.
- **Externalize your brain.** Sticky notes, whiteboards, paper. Don't try to hold things in your head — your working memory is precious, save it for the actual problem.
- **One project at a time.** Resist starting a second project until the first one is shipped. ADHD wants novelty. Discipline says finish.
- **Bad days are part of the plan.** You will have days where focus is impossible. Do 20 minutes of typing drills and call it a win. Streaks > intensity.

---

## Anti-Overwhelm Rules

- **If you miss a day, you do not "make it up."** Resume the next day. Guilt-driven double sessions kill plans.
- **If you finish a phase early, do not skip ahead.** Build a bonus project. Re-do problems. Mastery > speed.
- **If you finish a phase late, that's fine.** Not a race.
- **One day a week is rest.** No code, no guilt. Brain consolidates while you're not staring at a screen.
- **Once a month, do an honest review.** What feels solid? What feels shaky? Adjust the next month.

---

## On AI Tools (the hard part)

The plan is not "never use AI tools again." The plan is:

- **Months 1–4:** Zero AI tools while learning. Period. Uninstall Copilot. This is detox.
- **Months 5–6:** You may use AI to *review* code you've already written and got working. Ask it "what would you do differently?" Then evaluate critically — sometimes it's wrong, and you should be able to tell.
- **After the plan:** AI as a senior pair programmer, not a crutch. Test: if your AI tools disappeared tomorrow, could you still do your job? If yes, you're using them right.

---

## Your First Week (start the day after your bootcamp ends — give yourself 2 days off first)

1. Get a paper notebook. Label it "Learning Journal."
2. Get a kitchen timer or pomodoro app.
3. Get a wall calendar and a marker.
4. Install Python 3.12 + VS Code if you don't have them.
5. Make an Exercism account, join the Python track.
6. Day 1: Set a 90-minute timer. Solve the first 3 Exercism Python problems. Type every character yourself. No AI, no Stack Overflow until you're truly stuck.
7. End the session by writing in your journal: "I did it. Day 1 done." Mark the X on the calendar.

Day 2: Solve the next 3 Exercism problems. Re-solve one of yesterday's from memory. That's it.

You don't need to plan beyond that. Trust the structure.

---

## Free Resources, the Library, and Your Bootcamp

- **Las Vegas-Clark County Library** lends technical books for free via the **Libby** app — you have a card or can get one in 5 minutes. Worth knowing if you ever want a paper book to dog-ear.
- **Ask UNLV this week** if your bootcamp gives you continued access to any learning platforms (O'Reilly Learning, LinkedIn Learning, etc.) after graduation. Many do, and grads forget to use it. O'Reilly in particular has every technical book worth reading.

---

You've already done the hardest part: you noticed something was wrong, you asked for help, and you were honest about how your brain works. Most people fight their brain forever. You're about to start working *with* it. The overwhelm will fade as soon as you start doing instead of consuming. In six months you'll be a different engineer.
