# New service categories (MMA, fitness, weight loss, group fitness) and the video library.
# Videos are Coach Don's own Instagram reels, re-encoded for the web.

# key: (file stem in /videos, title, description, upload date, ISO duration, orientation)
VIDEOS = {
    "squats": ("squats-leg-day-strength-training-nairobi", "Leg day squats with progressive overload",
               "Coach Don takes a client through squats, from the 20 kg bar up to heavier sets, in a Nairobi gym.",
               "2026-09-22", "PT1M", "v"),
    "mma_speed": ("mma-striking-speed-drill-nairobi", "MMA striking speed drill: your POV facing speedy attacks",
                  "Coach Don Michael Ondiro throws fast MMA-style strikes and kicks straight at the camera during a gym session in Nairobi.",
                  "2026-09-17", "PT20S", "v"),
    "mma_pads": ("mma-boxing-pad-work-nairobi", "MMA and boxing pad work on a Nairobi rooftop",
                 "Live pad work session with a training partner: punches, kicks and footwork, coached by Don Michael Ondiro.",
                 "2026-07-25", "PT29S", "v"),
    "jkd_kicks": ("jeet-kune-do-kicks-nairobi", "Jeet Kune Do kicking drills: Just Listen",
                  "Black-and-white Jeet Kune Do training video showing kicks, footwork and combinations by Coach Don in Nairobi.",
                  "2026-10-03", "PT1M19S", "v"),
    "shadow": ("shadow-boxing-rooftop-nairobi", "Shadow boxing on the rooftop: repetition breeds mastery",
               "Use your space anywhere and anytime to do repetitions. Rooftop shadow boxing and striking practice in Nairobi.",
               "2026-09-22", "PT22S", "v"),
    "one_arm": ("one-arm-push-up-both-arms-nairobi", "The perfect one-arm push-up challenge (both sides)",
                "Straight down, straight up, both arms. Coach Don demonstrates strict one-arm push-ups on each side.",
                "2026-09-24", "PT22S", "v"),
    "variations": ("push-up-variations-calisthenics-nairobi", "Push-up variations to skyrocket your strength",
                   "Once you can do regular push-ups well, progress to harder variations. Calisthenics push-up progressions demonstrated in Nairobi.",
                   "2026-08-04", "PT39S", "h"),
    "hundred": ("100-push-up-challenge-nairobi", "0 to 100 push-up challenge",
                "100 push-ups a day keeps your weakness away. Coach Don takes on the 0 to 100 push-up challenge.",
                "2026-09-23", "PT57S", "v"),
    "gym_vars": ("gym-push-up-variations-challenge-nairobi", "Push-up challenge: only one person can do this",
                 "Advanced push-up and dumbbell variations performed in a Nairobi gym. Another day, another push-up.",
                 "2026-05-19", "PT39S", "v"),
    "gym_endurance": ("gym-strength-endurance-workout-nairobi", "Strength and endurance gym workout",
                      "Both physical and spiritual endurance are gifts from God. Take care of His temple. A gym strength and endurance session in Nairobi.",
                      "2025-09-12", "PT37S", "v"),
    "headstand": ("headstand-calisthenics-training-nairobi", "Tripod headstand: balance, control and core strength",
                  "Coach Don Michael Ondiro sets up a tripod on the mat, lifts into a full headstand with legs straight overhead, then lowers with control. Calisthenics skill training in a Nairobi gym.",
                  "2026-10-19", "PT19S", "v"),
    "partner": ("partner-push-up-challenge-nairobi", "Partner push-up challenge (Hapa Pale)",
                "Tag who you are trying this with. A fun partner push-up challenge for training with a friend.",
                "2026-08-24", "PT33S", "v"),
}

# Each video sits on the category it actually shows. Categories with no matching
# footage yet (kids, mobility) use photos only until the client sends videos.
VIDEO_FOR = {
    "personal-training": ["squats", "gym_endurance"],
    "fitness-training": ["squats", "gym_vars"],
    "mma-training": ["mma_speed", "mma_pads"],
    "aerobics-cardio": ["shadow"],
    "jeet-kune-do-martial-arts": ["jkd_kicks"],
    "boxing-kickboxing-fitness": ["mma_pads", "shadow"],
    "calisthenics-training": ["headstand", "variations"],
    "weight-loss-training": ["hundred"],
    "strength-conditioning": ["squats", "gym_endurance"],
    "group-fitness": ["partner"],
    "kids-teens-fitness": [],
    "mobility-flexibility": [],
}
# Primary category for each video (used for the label on the Videos page)
VIDEO_CATEGORY = {
    "squats": "fitness-training", "mma_speed": "mma-training", "mma_pads": "boxing-kickboxing-fitness",
    "jkd_kicks": "jeet-kune-do-martial-arts", "shadow": "aerobics-cardio", "one_arm": "calisthenics-training", "headstand": "calisthenics-training",
    "variations": "calisthenics-training", "hundred": "weight-loss-training", "gym_vars": "fitness-training",
    "gym_endurance": "strength-conditioning", "partner": "group-fitness",
}

# Display order of all categories (existing + new)
ORDER = ["personal-training", "fitness-training", "mma-training", "aerobics-cardio", "jeet-kune-do-martial-arts",
         "boxing-kickboxing-fitness", "calisthenics-training", "weight-loss-training", "strength-conditioning",
         "group-fitness", "kids-teens-fitness", "mobility-flexibility"]

NEW_SERVICES = [
    {
        "slug": "mma-training",
        "name": "MMA Training",
        "short": "MMA Training",
        "kw": "MMA training Nairobi",
        "img": "pads",
        "icon": "glove",
        "blurb": "Mixed martial arts fitness: striking, kicks, clinch basics and fight conditioning, for beginners and enthusiasts.",
        "title": "BEST MMA Training Nairobi | Mixed Martial Arts Classes, MMA Fitness & Striking Coach near me at D Dynamic Fitness",
        "meta": "MMA training in Nairobi with coach Don Michael Ondiro. Learn striking, kicks, defence and fight conditioning in beginner-friendly mixed martial arts sessions.",
        "h1": "MMA Training in Nairobi: Mixed Martial Arts Coaching",
        "intro": [
            "Mixed martial arts brings together the best of striking and grappling into one complete system. It is also a hard, rewarding way to get fit. You build power, stamina, coordination and the confidence that comes from knowing how to handle yourself.",
            "Coach Don Michael Ondiro trains in leisure MMA alongside Jeet Kune Do. His MMA sessions at D Dynamic Fitness focus on practical skills and hard conditioning, delivered in a controlled, beginner-friendly way. You do not need to want to fight in a cage. Most clients train MMA for fitness, self-defence and the challenge.",
        ],
        "sections": [
            ("What MMA training covers", """
<ul>
<li><strong>Stand-up striking:</strong> jab, cross, hooks, uppercuts, elbows and knees.</li>
<li><strong>Kicks:</strong> low kicks, body kicks, front kicks and switch kicks.</li>
<li><strong>Footwork and range:</strong> moving in and out of striking distance safely.</li>
<li><strong>Defence:</strong> slips, blocks, checks and getting off the line of attack.</li>
<li><strong>Clinch and takedown awareness:</strong> basic positions, balance and how to stay on your feet.</li>
<li><strong>Fight conditioning:</strong> round-based intervals that build MMA-specific stamina.</li>
</ul>"""),
            ("Watch: speed and pad work", """
<p>Both videos are from Coach Don's own training. The first puts you in front of fast strikes. The second is live pad work, the core of every MMA session, where the coach sets the pace, calls combinations and corrects technique as you go.</p>"""),
            ("MMA training levels", """
<table>
<thead><tr><th>Level</th><th>Focus</th><th>Who it suits</th></tr></thead>
<tbody>
<tr><td>Foundation</td><td>Stance, footwork, basic punches and kicks, conditioning</td><td>Complete beginners and fitness-focused clients</td></tr>
<tr><td>Intermediate</td><td>Combinations, defence, counters, clinch awareness</td><td>Clients with a few months of training</td></tr>
<tr><td>Advanced</td><td>Timing, flow drills, controlled partner work, optional light sparring</td><td>Committed students who want to test their skills</td></tr>
</tbody>
</table>"""),
            ("A typical MMA session", """
<ol>
<li><strong>Warm-up (10 min):</strong> skipping, joint mobility, shadow boxing.</li>
<li><strong>Technique (15 min):</strong> one striking or defensive skill, broken down and drilled.</li>
<li><strong>Pad rounds (15 min):</strong> 3-minute rounds putting the skill together at speed.</li>
<li><strong>Conditioning (10 min):</strong> sprawls, push-up variations, core and carries.</li>
<li><strong>Cool-down (5 min):</strong> stretching for hips, shoulders and neck.</li>
</ol>"""),
            ("Why MMA is a great workout", """
<p>MMA training uses your whole body in every round: legs to drive kicks, hips to generate power, core to link it all and shoulders to keep your guard up. It combines strength, cardio and skill, so sessions never feel like a chore.</p>
<ul>
<li>Burns a large number of calories per session.</li>
<li>Builds functional strength and explosive power.</li>
<li>Improves balance, coordination and reaction time.</li>
<li>Develops mental toughness and discipline.</li>
<li>Gives you practical self-defence skills.</li>
</ul>"""),
            ("Safety first", """
<p>Every session is controlled and supervised. Contact is never forced, and any partner work is introduced gradually with appropriate protective equipment. The goal is to train hard and come back next week, not to get hurt. If you have any injuries, tell your coach before your first session.</p>
<p>MMA pairs naturally with <a href="{root}services/jeet-kune-do-martial-arts.html">Jeet Kune Do</a> for striking efficiency and <a href="{root}services/strength-conditioning.html">strength and conditioning</a> for power. Want striking without the clinch? Try <a href="{root}services/boxing-kickboxing-fitness.html">boxing and kickboxing fitness</a>.</p>"""),
            ("MMA training across Nairobi", """
<p>We coach MMA and martial arts clients across the city, including <a href="{root}areas/parklands.html">Parklands</a> and <a href="{root}areas/kileleshwa.html">Kileleshwa</a>. Students, young professionals and families all train with us, so you will be in good company whatever your level.</p>"""),
        ],
        "faqs": [
            ("Do I have to spar in MMA training?", "No. Sparring is completely optional and only introduced once you have solid basics and want it. Many clients train MMA purely for fitness and self-defence."),
            ("Is MMA training suitable for beginners?", "Yes. Foundation sessions start with stance, footwork and basic strikes, scaled to your fitness level."),
            ("What equipment do I need for MMA?", "Start with comfortable clothes, hand wraps and a water bottle. MMA gloves, shin guards and a mouthguard are recommended as you progress. We will advise what to buy."),
            ("What is the difference between MMA and Jeet Kune Do?", "Jeet Kune Do is a martial art philosophy focused on efficient, direct striking. MMA is a broader sport combining striking with clinch and ground skills. Coach Don trains both and blends their best ideas."),
            ("Can women and teenagers train MMA?", "Yes. Sessions are adapted for every age and level, with a strong focus on technique, control and safety."),
        ],
    },
    {
        "slug": "fitness-training",
        "name": "Fitness & Weight Training",
        "short": "Fitness Training",
        "kw": "fitness trainer Nairobi",
        "img": "core",
        "icon": "dumbbell",
        "blurb": "Get fitter and stronger with free weights, machines and structured programmes for muscle and strength.",
        "title": "BEST Fitness Trainer Nairobi | Weight Training, Muscle Building & Fitness Programmes near me at D Dynamic Fitness",
        "meta": "Fitness and weight training coach in Nairobi. Learn proper lifting technique, build muscle and get stronger with structured fitness programmes from coach Don Michael Ondiro.",
        "h1": "Fitness Trainer in Nairobi: Weight Training & Muscle Building",
        "intro": [
            "Training in a gym without a plan wastes your membership. Machines you are not sure how to use, a crowded free-weights area and random workouts that never seem to change anything. Fitness training with D Dynamic Fitness fixes that.",
            "Coach Don Michael Ondiro teaches you how to train properly: the right exercises, the right technique and a programme that progresses every week. You will know what you did in every session and why.",
        ],
        "sections": [
            ("What fitness training includes", """
<ul>
<li><strong>Gym orientation:</strong> how to use free weights, cables and machines safely.</li>
<li><strong>Technique coaching</strong> on the key lifts: squat, deadlift, bench press, overhead press, rows and pull-ups.</li>
<li><strong>A written programme</strong> with sets, reps and weights that progress each week.</li>
<li><strong>Muscle-building principles:</strong> volume, intensity, tempo and recovery explained simply.</li>
<li><strong>Gym etiquette and confidence:</strong> so the weights room never feels intimidating again.</li>
</ul>"""),
            ("Watch: squats and strength work", """
<p>The first video is a real client session: squats with progressive overload, starting with the 20 kg bar and adding weight set by set while Don coaches her form. The second is Don's own training with push-up and dumbbell variations.</p>"""),
            ("A sample 4-day training split", """
<table>
<thead><tr><th>Day</th><th>Focus</th><th>Example exercises</th></tr></thead>
<tbody>
<tr><td>Monday</td><td>Upper body push</td><td>Bench press, overhead press, dips, triceps work</td></tr>
<tr><td>Tuesday</td><td>Lower body</td><td>Squats, Romanian deadlifts, lunges, calf raises</td></tr>
<tr><td>Thursday</td><td>Upper body pull</td><td>Pull-ups, rows, face pulls, biceps work</td></tr>
<tr><td>Friday</td><td>Full body and conditioning</td><td>Deadlifts, push-up variations, carries, intervals</td></tr>
</tbody>
</table>
<p>Your programme is built around how many days you can train. Two or three full-body sessions a week work very well for most people.</p>"""),
            ("How progressive overload works", """
<p>Muscles grow and get stronger when they are asked to do a little more over time. That is progressive overload, and it is the single most important principle in fitness training. Your programme builds it in through:</p>
<ol>
<li>Adding a small amount of weight when you hit your target reps.</li>
<li>Adding reps or sets at the same weight.</li>
<li>Improving technique, range of motion and control.</li>
<li>Reducing rest periods for conditioning blocks.</li>
</ol>
<p>Every session is logged, so you can see your numbers climb week after week.</p>"""),
            ("Common training mistakes we fix", """
<ul>
<li><strong>Ego lifting:</strong> too much weight, poor form, high injury risk.</li>
<li><strong>Program hopping:</strong> changing workouts every week so nothing progresses.</li>
<li><strong>Skipping legs:</strong> leg training builds overall strength and burns more energy.</li>
<li><strong>No warm-up:</strong> a few minutes of preparation makes every set safer and stronger.</li>
<li><strong>Not eating enough protein</strong> to recover and build muscle.</li>
</ul>"""),
            ("Gym training plus the rest of your week", """
<p>Gym training combines well with other services. Add <a href="{root}services/calisthenics-training.html">calisthenics</a> for relative strength, <a href="{root}services/mobility-flexibility.html">mobility training</a> to lift in better positions, or <a href="{root}services/weight-loss-training.html">weight loss coaching</a> if fat loss is your main goal. We train fitness clients across Nairobi, including <a href="{root}areas/westlands.html">Westlands</a> and <a href="{root}areas/kilimani.html">Kilimani</a>.</p>"""),
            ("Checklist for your first session", """
<ul class="ticks">
<li>Comfortable training clothes and supportive trainers</li>
<li>Water bottle and a small towel</li>
<li>A light meal one to two hours before</li>
<li>Your goals, and any injuries or health conditions to discuss</li>
<li>Your gym membership details, if training at a commercial gym</li>
</ul>"""),
        ],
        "faqs": [
            ("Do I need a gym membership to train with you?", "It depends on where you want to train. Message on WhatsApp with your location and we will advise the best set-up for gym-based sessions."),
            ("How long does it take to build muscle?", "Most beginners notice strength gains within a few weeks and visible muscle changes within two to three months of consistent training and good nutrition."),
            ("Will lifting weights make women bulky?", "No. Weight training helps women build strength and a toned shape. Getting bulky takes years of very specific training and eating."),
            ("Can you write me a fitness programme to follow on my own?", "Yes. Programmes can combine a few coached sessions with workouts you do on your own, with regular check-ins to adjust the plan."),
        ],
    },
    {
        "slug": "weight-loss-training",
        "name": "Weight Loss & Fat Loss Training",
        "short": "Weight Loss Training",
        "kw": "weight loss trainer Nairobi",
        "img": "rooftop",
        "icon": "flame",
        "blurb": "A realistic fat loss plan: coached training, daily movement and simple nutrition built around Kenyan food.",
        "title": "BEST Weight Loss Trainer Nairobi | Fat Loss Programmes, Body Transformation & Fitness Coaching near me at D Dynamic Fitness",
        "meta": "Weight loss personal trainer in Nairobi. Lose fat and keep it off with coached workouts, simple nutrition guidance and accountability from coach Don Michael Ondiro.",
        "h1": "Weight Loss Trainer in Nairobi: Fat Loss Coaching",
        "intro": [
            "Losing weight is hard to keep up. Crash diets, endless cardio and 30-day challenges might move the scale for a while, but most people end up back where they started. Lasting fat loss needs a plan you can keep up.",
            "Weight loss coaching at D Dynamic Fitness combines three things: strength-based training that protects your muscle, daily movement that adds up, and simple nutrition built around the food you already eat. Coach Don Michael Ondiro keeps you accountable every week, so progress keeps coming.",
        ],
        "sections": [
            ("The three pillars of fat loss", """
<table>
<thead><tr><th>Pillar</th><th>What it means</th><th>Why it matters</th></tr></thead>
<tbody>
<tr><td>Training</td><td>Two to four strength and conditioning sessions a week</td><td>Keeps muscle while you lose fat, so you look toned</td></tr>
<tr><td>Movement</td><td>Daily steps, walking and active hobbies</td><td>Burns more energy across the week than workouts alone</td></tr>
<tr><td>Nutrition</td><td>A modest calorie deficit with plenty of protein</td><td>Fat loss happens in the kitchen. Training makes it look good.</td></tr>
</tbody>
</table>"""),
            ("Watch: the 100 push-up challenge", """
<p>Don's motto for this one: "100 push-ups a day keeps your weakness away." Small daily habits add up. Short bursts of movement through the day, like push-ups, squats and a lunchtime walk, burn more energy than most people expect.</p>"""),
            ("What a weight loss programme looks like", """
<ol>
<li><strong>Starting point:</strong> measurements, photos, current habits and a realistic goal.</li>
<li><strong>Training plan:</strong> full-body strength sessions with conditioning finishers.</li>
<li><strong>Step target:</strong> a daily movement goal that increases gradually.</li>
<li><strong>Nutrition basics:</strong> portion guidance, protein targets and simple swaps.</li>
<li><strong>Weekly check-ins:</strong> adjust the plan based on your results.</li>
</ol>"""),
            ("Eating for fat loss in Kenya", """
<p>You do not need to give up ugali or chapati to lose weight. You need to know how much fits your goal and what to pair it with. Simple rules most clients follow:</p>
<ul>
<li>Fill half your plate with vegetables such as sukuma, cabbage, spinach or a kachumbari salad.</li>
<li>Add a palm-sized portion of protein: beans, ndengu, eggs, fish, chicken or lean beef.</li>
<li>Keep starches like ugali, rice, chapati and potatoes to a fist-sized portion.</li>
<li>Cut back on sugary tea, sodas and juices. They add up quickly.</li>
<li>Go easy on fried foods and choose grilled or boiled where possible.</li>
<li>Drink water through the day.</li>
</ul>"""),
            ("Why strength training beats endless cardio", """
<p>Cardio burns energy while you do it. Strength training builds and keeps muscle, which shapes your body as fat comes off and supports a healthy metabolism. The best fat loss programmes use both, with strength as the foundation and conditioning such as <a href="{root}services/boxing-kickboxing-fitness.html">boxing pad rounds</a> or circuits on top.</p>"""),
            ("Staying on track", """
<ul class="ticks">
<li>Aim for steady progress of around 0.5 to 1 kg a week, not dramatic drops.</li>
<li>Track waist measurements and photos, as well as the scale.</li>
<li>Plan for weekends, weddings and celebrations. They are part of life.</li>
<li>Sleep well, because poor sleep increases hunger and cravings.</li>
<li>Focus on habits you can keep for years, not weeks.</li>
</ul>
<p>Weight loss clients often combine this programme with <a href="{root}services/personal-training.html">one-on-one personal training</a> or <a href="{root}services/group-fitness.html">group and partner sessions</a>. We coach clients across Nairobi, including <a href="{root}areas/lavington.html">Lavington</a> and <a href="{root}areas/kilimani.html">Kilimani</a>.</p>"""),
        ],
        "faqs": [
            ("How fast can I lose weight?", "A healthy, sustainable rate for most people is around 0.5 to 1 kg per week. Faster loss is usually water and muscle, and tends to come back."),
            ("Do I have to stop eating ugali and chapati?", "No. You learn portion sizes that fit your goal and pair starches with protein and vegetables."),
            ("Will I need supplements?", "No. Supplements are optional. Real food, good sleep and consistent training do the heavy lifting."),
            ("Can I lose belly fat specifically?", "You can't spot-reduce fat, but overall fat loss through training and nutrition will reduce belly fat over time."),
        ],
    },
    {
        "slug": "group-fitness",
        "name": "Group & Partner Fitness Classes",
        "short": "Group Fitness",
        "kw": "group fitness classes Nairobi",
        "img": "partner",
        "icon": "group",
        "blurb": "Train with friends, family or colleagues: fun, coached small-group sessions that share the cost and the motivation.",
        "title": "BEST Group Fitness Classes Nairobi | Partner Training, Small Group & Corporate Fitness Sessions near me at D Dynamic Fitness",
        "meta": "Small-group, partner and corporate fitness sessions in Nairobi. Train with friends or colleagues, share the cost and stay motivated with coach Don Michael Ondiro.",
        "h1": "Group Fitness Classes in Nairobi: Partner & Small-Group Training",
        "intro": [
            "Training with other people helps. A partner or small group makes sessions more fun, keeps everyone accountable and makes professional coaching more affordable. You push a little harder when someone next to you is pushing too.",
            "D Dynamic Fitness runs coached partner and small-group sessions for friends, couples, families and teams. Coach Don Michael Ondiro keeps the group moving with challenges, circuits and pad work, while still adjusting every exercise to each person's level.",
        ],
        "sections": [
            ("Group training options", """
<table>
<thead><tr><th>Format</th><th>Group size</th><th>Best for</th></tr></thead>
<tbody>
<tr><td>Partner training</td><td>2 people</td><td>Couples, friends and training buddies</td></tr>
<tr><td>Small group</td><td>3 to 6 people</td><td>Friends, neighbours and families</td></tr>
<tr><td>Corporate fitness</td><td>By arrangement</td><td>Office teams and wellness programmes</td></tr>
<tr><td>Youth martial arts groups</td><td>By arrangement</td><td>Teenagers and children learning discipline and fitness</td></tr>
</tbody>
</table>"""),
            ("Watch: the partner challenge", """
<p>Group sessions often finish with a challenge like this partner push-up drill. Competitive, a bit silly and hard work. Tag the person you would try it with.</p>"""),
            ("What a group session looks like", """
<ol>
<li><strong>Team warm-up:</strong> movement games and mobility to get everyone going.</li>
<li><strong>Skill block:</strong> learning a lift, a calisthenics progression or a striking combination.</li>
<li><strong>Circuit or pad rounds:</strong> stations or partner drills with work-and-rest intervals.</li>
<li><strong>Challenge finisher:</strong> a partner or team challenge to end on a high.</li>
<li><strong>Cool-down:</strong> stretching and a quick chat about the week ahead.</li>
</ol>"""),
            ("Benefits of training together", """
<ul>
<li><strong>Lower cost per person</strong> than one-on-one coaching.</li>
<li><strong>Built-in accountability:</strong> it is harder to skip when your friends are waiting.</li>
<li><strong>More fun:</strong> challenges and team drills make the hour fly by.</li>
<li><strong>Still personal:</strong> every exercise is scaled for each person's level.</li>
<li><strong>Community:</strong> many clients make new training friends.</li>
</ul>"""),
            ("Corporate fitness and team building", """
<p>Healthy, energised teams work better. D Dynamic Fitness can run regular staff fitness sessions or one-off team-building workouts for Nairobi companies, built around boxing fitness, bodyweight circuits and partner challenges that anyone can join. Contact us on WhatsApp to discuss your team's needs.</p>"""),
            ("Mix and match", """
<p>Group sessions can focus on <a href="{root}services/calisthenics-training.html">calisthenics</a>, <a href="{root}services/boxing-kickboxing-fitness.html">boxing fitness</a>, <a href="{root}services/mma-training.html">MMA conditioning</a> or general <a href="{root}services/weight-loss-training.html">fat loss</a>. Popular with groups in <a href="{root}areas/parklands.html">Parklands</a> and <a href="{root}areas/karen.html">Karen</a>.</p>"""),
        ],
        "faqs": [
            ("How many people can join a group session?", "Small groups are usually 3 to 6 people so everyone still gets coaching attention. Larger corporate sessions can be arranged."),
            ("Can people with different fitness levels train together?", "Yes. Every exercise has easier and harder versions, so beginners and experienced clients can train side by side."),
            ("Do you run corporate wellness sessions?", "Yes, by arrangement. Message on WhatsApp with your team size, location and goals."),
            ("Is group training cheaper than personal training?", "Yes. The cost is shared, which makes coached training more affordable per person."),
        ],
    },
    {
        "slug": "aerobics-cardio",
        "name": "Aerobics & Cardio Fitness Classes",
        "short": "Aerobics & Cardio",
        "kw": "aerobics classes Nairobi",
        "img": "shadow",
        "icon": "heart",
        "blurb": "High-energy aerobics, HIIT and cardio-boxing sessions to boost stamina, burn calories and lift your mood.",
        "title": "BEST Aerobics Classes Nairobi | Cardio Fitness, HIIT, Step & Cardio Boxing Workouts near me at D Dynamic Fitness",
        "meta": "Aerobics and cardio fitness classes in Nairobi. HIIT, cardio boxing and aerobic circuits to build stamina and burn fat, coached by Don Michael Ondiro.",
        "h1": "Aerobics Classes in Nairobi: Cardio & HIIT Fitness",
        "intro": [
            "Aerobics is one of the most popular ways to get fit in Nairobi. Upbeat, energetic cardio sessions strengthen your heart and lungs, burn a lot of energy and leave you feeling great. They are also more fun than a treadmill.",
            "D Dynamic Fitness aerobics and cardio sessions blend classic aerobic movement with HIIT intervals, bodyweight circuits and cardio boxing inspired by Coach Don Michael Ondiro's martial arts background. Every session is scaled to your fitness, so beginners and regulars can train side by side.",
        ],
        "sections": [
            ("Types of cardio sessions", """
<table>
<thead><tr><th>Session</th><th>What it involves</th><th>Best for</th></tr></thead>
<tbody>
<tr><td>Aerobic circuits</td><td>Continuous rhythmic movement: steps, jacks, knee drives, lunges</td><td>Building stamina and a fitness base</td></tr>
<tr><td>HIIT</td><td>Short hard intervals with rest: sprints, burpees, squat jumps</td><td>Burning maximum energy in less time</td></tr>
<tr><td>Cardio boxing</td><td>Shadow boxing, punch combos and kicks to the beat</td><td>Fun, stress relief and coordination</td></tr>
<tr><td>Low-impact cardio</td><td>Joint-friendly movements without jumping</td><td>Beginners, older adults and heavier clients</td></tr>
</tbody>
</table>"""),
            ("Watch: rooftop shadow boxing", """
<p>Non-stop shadow boxing is one of the cardio drills Don uses most. No equipment, any space, and your heart rate climbs within a minute. Cardio sessions mix this with aerobic circuits and intervals.</p>"""),
            ("Benefits of aerobics and cardio training", """
<ul>
<li><strong>Stronger heart and lungs</strong> and better everyday stamina.</li>
<li><strong>Fat loss support</strong> through high energy burn.</li>
<li><strong>Better mood and lower stress</strong>, thanks to the endorphin rush.</li>
<li><strong>Improved coordination</strong> from rhythmic and boxing movements.</li>
<li><strong>Better sleep</strong> and more energy through the day.</li>
</ul>"""),
            ("A typical 45-minute aerobics session", """
<ol>
<li><strong>Warm-up (7 min):</strong> marching, arm circles and light rhythmic moves.</li>
<li><strong>Aerobic block (15 min):</strong> continuous combinations building in intensity.</li>
<li><strong>Cardio boxing (10 min):</strong> jabs, crosses, hooks and kicks in rounds.</li>
<li><strong>HIIT finisher (8 min):</strong> short intervals scaled to your level.</li>
<li><strong>Cool-down (5 min):</strong> slow walking and stretching.</li>
</ol>"""),
            ("Aerobics for every level", """
<p>Every movement has an easier and a harder option. Beginners start with low-impact versions and longer rests; regulars add jumps, speed and shorter rests. If you are new to exercise or managing a health condition, tell your coach so the session can be adjusted. For best results, combine cardio with <a href="{root}services/fitness-training.html">fitness and weight training</a> to keep muscle while you burn fat.</p>"""),
            ("Group aerobics and cardio", """
<p>Cardio sessions work brilliantly in a group: the energy is contagious. Ask about <a href="{root}services/group-fitness.html">group and partner sessions</a> for friends, church groups or office teams. Aimed at fat loss? See our <a href="{root}services/weight-loss-training.html">weight loss programme</a>. We run cardio sessions for clients across Nairobi, including <a href="{root}areas/kilimani.html">Kilimani</a> and <a href="{root}areas/westlands.html">Westlands</a>.</p>"""),
            ("Tips for your first aerobics class", """
<ul class="ticks">
<li>Wear supportive trainers with good cushioning.</li>
<li>Bring plenty of water. You will sweat.</li>
<li>Eat lightly one to two hours before.</li>
<li>Go at your own pace and take the low-impact option when you need it.</li>
<li>Come back consistently. Stamina builds fast with regular sessions.</li>
</ul>"""),
        ],
        "faqs": [
            ("Are aerobics classes good for weight loss?", "Yes. Aerobics and HIIT burn a lot of energy and, combined with sensible eating and some strength training, are very effective for fat loss."),
            ("I'm not coordinated. Can I still do aerobics?", "Absolutely. Moves are taught step by step and kept simple. Coordination improves quickly with practice."),
            ("Is there a low-impact option?", "Yes. Every session includes joint-friendly alternatives without jumping."),
            ("How often should I do cardio?", "Two to four cardio sessions a week alongside strength training works well for most people."),
        ],
    },
    {
        "slug": "kids-teens-fitness",
        "name": "Kids & Teens Fitness and Martial Arts",
        "short": "Kids & Teens Fitness",
        "kw": "kids martial arts Nairobi",
        "img": "kick",
        "icon": "kids",
        "blurb": "Fun, safe fitness and martial arts sessions that build confidence, discipline and coordination in young people.",
        "title": "BEST Kids Martial Arts & Fitness Classes Nairobi | Teen Self-Defence, Sports Fitness & Confidence Training near me at D Dynamic Fitness",
        "meta": "Kids and teens fitness and martial arts in Nairobi. Safe, fun sessions that build confidence, discipline, coordination and self-defence skills with coach Don.",
        "h1": "Kids & Teens Martial Arts and Fitness in Nairobi",
        "intro": [
            "Children and teenagers today spend more time sitting than ever, between school, homework and screens. Fitness and martial arts training gets them moving, builds real confidence and teaches lessons in discipline and respect that carry into every part of life.",
            "D Dynamic Fitness offers age-appropriate sessions for young people, drawing on Coach Don Michael Ondiro's Jeet Kune Do, calisthenics and coaching background. Sessions are fun, safe and structured, with a strong focus on control, good character and age-appropriate effort.",
        ],
        "sections": [
            ("What young people learn", """
<ul>
<li><strong>Martial arts basics:</strong> stance, footwork, strikes and kicks on pads, never on each other without supervision.</li>
<li><strong>Self-defence awareness:</strong> staying safe, avoiding trouble and confident body language.</li>
<li><strong>Bodyweight fitness:</strong> push-ups, squats, jumping and core work through games and challenges.</li>
<li><strong>Coordination and agility:</strong> balance, reaction drills and ladder work.</li>
<li><strong>Discipline and respect:</strong> listening, focus, effort and good sportsmanship.</li>
</ul>"""),
            ("Sessions by age group", """
<table>
<thead><tr><th>Age</th><th>Focus</th></tr></thead>
<tbody>
<tr><td>Younger children</td><td>Movement games, balance, coordination, basic strikes on pads, listening skills</td></tr>
<tr><td>Pre-teens</td><td>Martial arts technique, bodyweight strength, agility, confidence</td></tr>
<tr><td>Teenagers</td><td>Jeet Kune Do and boxing skills, sports conditioning, self-defence, healthy habits</td></tr>
</tbody>
</table>
<p>Exact groupings depend on the children's ages and experience. Ask on WhatsApp for current options.</p>"""),
            ("Benefits for children and teens", """
<ul>
<li>Higher self-confidence and self-esteem.</li>
<li>Better focus, which often helps at school.</li>
<li>Healthy outlet for energy and stress.</li>
<li>Stronger bodies and better coordination for every sport.</li>
<li>Practical safety skills and awareness.</li>
<li>Positive role model and structure.</li>
</ul>"""),
            ("Sports fitness for young athletes", """
<p>Teenagers playing football, rugby, basketball or athletics at school benefit hugely from learning to move, land and lift correctly. Age-appropriate <a href="{root}services/strength-conditioning.html">strength and conditioning</a> focuses on technique, bodyweight skills and injury prevention before heavy loads.</p>"""),
            ("Safety and supervision", """
<p>Safety comes first in every session. Contact is controlled and supervised, equipment is age-appropriate, and parents are welcome to discuss any concerns. Sessions can be private, sibling or small-group, popular with families in <a href="{root}areas/kileleshwa.html">Kileleshwa</a> and <a href="{root}areas/lavington.html">Lavington</a>. Adults can join too in our <a href="{root}services/jeet-kune-do-martial-arts.html">Jeet Kune Do</a> and <a href="{root}services/group-fitness.html">family group sessions</a>.</p>"""),
        ],
        "faqs": [
            ("What age can my child start?", "It depends on the child. Message on WhatsApp with your child's age and we will recommend the right format."),
            ("Will martial arts make my child aggressive?", "No. Good martial arts training teaches control, respect and avoiding conflict. Most parents notice their children become calmer and more confident."),
            ("Can siblings train together?", "Yes. Sibling and small family-group sessions are available by arrangement."),
            ("Can parents watch?", "Yes. Parents are welcome, and we are happy to talk through progress after sessions."),
        ],
    },
]

# Icons for each service card (inline SVG paths, 24x24 viewBox)
ICONS = {
    "personal-training": "M12 2a3 3 0 1 1 0 6 3 3 0 0 1 0-6Zm-6 20v-6l-2-1 2-6h12l2 6-2 1v6h-3v-6h-6v6Z",
    "fitness-training": "M2 10h2V8h2v8H4v-2H2v-4Zm4-3h3v10H6V7Zm4 4h4v2h-4v-2Zm5-4h3v10h-3V7Zm3 1h2v2h2v4h-2v2h-2V8Z",
    "mma-training": "M7 4h7a4 4 0 0 1 4 4v2a3 3 0 0 1-1 2.2V17a3 3 0 0 1-3 3H9a3 3 0 0 1-3-3v-3H5a2 2 0 0 1-2-2V9a2 2 0 0 1 2-2h1V5a1 1 0 0 1 1-1Zm1 3v4h7V8a1 1 0 0 0-1-1H8Z",
    "jeet-kune-do-martial-arts": "M14 3a2 2 0 1 1 0 4 2 2 0 0 1 0-4Zm-3.5 5h4l3 3 3.5-1 .5 2-4.5 1.5-2-2-1 3 3 3v4.5h-2v-3.7l-3-2.8-1.5 3.5H4v-2h5.2L11 9.6l-1.8.8L7.5 13l-1.7-1 2-3.3Z",
    "boxing-kickboxing-fitness": "M8 3h6a5 5 0 0 1 5 5v3a4 4 0 0 1-2 3.5V19a2 2 0 0 1-2 2H9a2 2 0 0 1-2-2v-3H6a3 3 0 0 1-3-3v-2a3 3 0 0 1 3-3h1V4a1 1 0 0 1 1-1Zm1 2v6h2V5H9Z",
    "calisthenics-training": "M3 4h18v2h-2v2h-2V6H7v2H5V6H3V4Zm9 4a2 2 0 1 1 0 4 2 2 0 0 1 0-4Zm-3 5h6l1 4-2 1-.5-2h-3l-.5 2-2-1 1-4Zm0 6h6v2H9v-2Z",
    "strength-conditioning": "M1 11h3V8h3v8H4v-3H1v-2Zm7-5h3v12H8V6Zm5 5h-1v2h1v-2Zm1-5h3v12h-3V6Zm4 2h3v3h2v2h-2v3h-3V8Z",
    "weight-loss-training": "M12 2s6 5 6 11a6 6 0 0 1-12 0c0-3 2-5 2-5s0 3 2 4c0-5 2-10 2-10Zm0 12c-1 1-2 2-2 3.5a2 2 0 0 0 4 0c0-1.5-1-2.5-2-3.5Z",
    "group-fitness": "M8 4a3 3 0 1 1 0 6 3 3 0 0 1 0-6Zm8 1a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5ZM2 20v-3a5 5 0 0 1 10 0v3H2Zm12 0v-3c0-1.3-.4-2.5-1-3.5a4 4 0 0 1 9 2.5v4h-8Z",
    "mobility-flexibility": "M12 2a2 2 0 1 1 0 4 2 2 0 0 1 0-4ZM4 8h16v2h-6v4l3 7h-2.2L12 15l-2.8 6H7l3-7v-4H4V8Z",
    "aerobics-cardio": "M12 21s-8-5.2-8-11a4.5 4.5 0 0 1 8-2.8A4.5 4.5 0 0 1 20 10c0 5.8-8 11-8 11Zm-5-10h2.5l1.5-2.5 2 5 1.5-2.5H17v-1.5h-3.2l-.8 1.4-2-5-2.3 3.6H7V11Z",
    "kids-teens-fitness": "M9 3a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5Zm7 3a2 2 0 1 1 0 4 2 2 0 0 1 0-4ZM5 21v-6l-1-1 2-5h6l2 5-1 1v6h-2.5v-5h-3v5H5Zm10 0v-4l-1-1 1.2-4h3.6L20 16l-1 1v4h-4Z",
}
