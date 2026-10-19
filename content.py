# Page copy for the D Dynamic Fitness site. build.py turns this into HTML.
# Services and areas below are drafts based on the coach's Instagram content.
# Confirm with the client which services they actually offer and which areas they cover.

IMG = {
    "portrait": ("don-michael-ondiro-personal-trainer-nairobi.jpg", "Don Michael Ondiro, certified personal trainer in Nairobi, smiling in the gym", 1200, 1200),
    "coach": ("coach-don-michael-ondiro-gym-nairobi.jpg", "Coach Don Michael Ondiro in a Nairobi gym", 1200, 1200),
    "curl": ("dumbbell-curl-fitness-training-nairobi.jpg", "Dumbbell curl during fitness and weight training in Nairobi", 1200, 1200),
    "mma_img": ("mma-training-striking-drill-nairobi.jpg", "MMA striking drill during a training session in Nairobi", 720, 1280),
    "boxing_img": ("boxing-shadow-boxing-workout-nairobi.jpg", "Rooftop shadow boxing workout in Nairobi", 720, 1280),
    "hundred_img": ("weight-loss-push-up-challenge-nairobi.jpg", "Push-up challenge for fat loss and fitness in Nairobi", 720, 1280),
    "core": ("personal-trainer-nairobi-gym-core-training.jpg", "Personal trainer in Nairobi doing a core strength drill in the gym", 361, 640),
    "turf": ("calisthenics-push-up-training-nairobi.jpg", "Calisthenics push-up training on gym turf in Nairobi", 360, 640),
    "kick": ("jeet-kune-do-kick-training-nairobi.jpg", "Jeet Kune Do kick training session with a Nairobi martial arts coach", 361, 640),
    "headstand": ("headstand-calisthenics-nairobi.jpg", "Coach Don holding a tripod headstand during calisthenics training in a Nairobi gym", 361, 640),
    "onearm": ("one-arm-push-up-calisthenics-nairobi.jpg", "One arm push-up calisthenics challenge on a Nairobi rooftop", 361, 640),
    "knuckle": ("bare-knuckle-push-up-challenge-nairobi.jpg", "Bare knuckle push-up challenge for martial arts conditioning in Nairobi", 361, 640),
    "squat": ("strength-training-client-squat-nairobi.jpg", "Personal training client squatting 60 kg during a strength session in Nairobi", 361, 640),
    "shadow": ("shadow-boxing-conditioning-nairobi.jpg", "Outdoor shadow boxing conditioning workout in Nairobi", 361, 640),
    "mobility": ("mobility-stick-shoulder-training-nairobi.jpg", "Shoulder mobility drill with a training stick at a Nairobi gym", 1200, 1200),
    "partner": ("partner-push-up-workout-nairobi-gym.jpg", "Partner push-up workout led by a Nairobi fitness coach", 361, 640),
    "rooftop": ("bodyweight-push-up-rooftop-workout-nairobi.jpg", "Bodyweight push-up workout outdoors in Nairobi", 640, 360),
    "pads": ("boxing-pad-work-session-nairobi.jpg", "Boxing pad work session with a client in Nairobi", 361, 640),
}

GALLERY = ["portrait", "curl", "kick", "squat", "onearm", "pads", "coach", "mobility", "turf", "knuckle", "shadow", "partner", "core", "rooftop"]

# Main image for each training category
CATEGORY_IMG = {
    "personal-training": "coach", "fitness-training": "curl", "mma-training": "mma_img", "aerobics-cardio": "shadow",
    "jeet-kune-do-martial-arts": "kick", "boxing-kickboxing-fitness": "boxing_img", "calisthenics-training": "headstand",
    "weight-loss-training": "rooftop", "strength-conditioning": "squat", "group-fitness": "partner",
    "kids-teens-fitness": "pads", "mobility-flexibility": "mobility",
}

# ---------------------------------------------------------------- services
SERVICES = [
    {
        "slug": "personal-training",
        "name": "One-on-One Personal Training",
        "short": "Personal Training",
        "kw": "personal trainer Nairobi",
        "img": "squat",
        "blurb": "Private sessions built around your goal, whether that is fat loss, muscle, strength or simply feeling fit again.",
        "title": "BEST Personal Trainer Nairobi | One-on-One Personal Training near me with Don Michael Ondiro at D Dynamic Fitness",
        "meta": "Certified personal trainer in Nairobi offering one-on-one sessions for fat loss, strength and muscle. Book a private training session with Don Michael Ondiro.",
        "h1": "Personal Trainer in Nairobi: One-on-One Training",
        "intro": [
            "Most gym plans fail because they were not written for you. One-on-one personal training with D Dynamic Fitness starts with your body, your schedule and your goal, then builds a plan that fits.",
            "Coach Don Michael Ondiro is a certified fitness and performance coach based in Nairobi. Every session is planned, coached and tracked, so you always know what you are doing, why you are doing it and how far you have come.",
        ],
        "sections": [
            ("What one-on-one training includes", """
<p>Your first session is an assessment, not a beat-down. We look at how you move, what your training history is, any old injuries and what you want to achieve in the next 12 weeks. From there you get a programme that fits the time you really have, whether that is two sessions a week or five.</p>
<ul>
<li><strong>Movement and fitness assessment</strong> covering posture, mobility, strength and conditioning.</li>
<li><strong>A written programme</strong> that progresses week by week, so you never plateau by guessing.</li>
<li><strong>Coached sessions</strong> with hands-on technique correction for every lift and drill.</li>
<li><strong>Simple nutrition guidance</strong> built around Kenyan food you already eat, not imported meal plans.</li>
<li><strong>Progress check-ins</strong> with measurements, photos and strength numbers.</li>
</ul>"""),
            ("Goals we train for", """
<p>Most clients come to a personal trainer in Nairobi with one of a few goals. Each one needs a different approach, and your programme is built around yours.</p>
<table>
<thead><tr><th>Goal</th><th>Main focus</th><th>Typical training mix</th></tr></thead>
<tbody>
<tr><td>Fat loss</td><td>Consistency and energy output</td><td>Strength circuits, conditioning, daily step targets</td></tr>
<tr><td>Muscle and tone</td><td>Progressive overload</td><td>Free weights, calisthenics, controlled tempo work</td></tr>
<tr><td>Strength</td><td>Technique on the big lifts</td><td>Squat, hinge, push and pull patterns with planned progressions</td></tr>
<tr><td>General fitness</td><td>Feeling and moving better</td><td>Mobility, bodyweight training, low-impact cardio</td></tr>
</tbody>
</table>"""),
            ("Why train with a coach instead of alone", """
<p>Training alone works for some people. For most, it stalls. A coach removes the guesswork, keeps you accountable on the days you would rather skip and spots the small technique faults that turn into injuries later.</p>
<p>Don's background in <a href="{root}services/jeet-kune-do-martial-arts.html">Jeet Kune Do and martial arts conditioning</a> means sessions stay athletic and varied. You will lift, but you will also learn to move well, breathe properly and build the kind of fitness that carries into everyday life.</p>"""),
            ("What a typical session looks like", """
<ol>
<li><strong>Warm-up and mobility (10 minutes):</strong> joint prep for the work ahead.</li>
<li><strong>Main strength block (25 minutes):</strong> your key lifts or calisthenics progressions.</li>
<li><strong>Conditioning finisher (10 minutes):</strong> intervals, carries or pad work.</li>
<li><strong>Cool-down and review (5 minutes):</strong> stretch, log the session, plan the next one.</li>
</ol>"""),
        ],
        "faqs": [
            ("How much does a personal trainer cost in Nairobi?", "Prices depend on how many sessions you book per week and where you train. Message D Dynamic Fitness on WhatsApp for current session and package rates."),
            ("Do I need to be fit before I start personal training?", "No. Programmes are built from your current level. Complete beginners are welcome, and the first session is an assessment so we know exactly where to start."),
            ("How many sessions a week do I need?", "Two to three coached sessions a week is enough for most people to see steady progress. We can add a home or solo plan for the days in between."),
            ("Can personal training help with fat loss?", "Yes. Fat loss comes from consistent training plus sensible eating. You get both a training programme and simple nutrition guidance built around food you already eat."),
        ],
    },
    {
        "slug": "calisthenics-training",
        "name": "Calisthenics & Bodyweight Training",
        "short": "Calisthenics Training",
        "kw": "calisthenics coach Nairobi",
        "img": "onearm",
        "blurb": "Master push-ups, pull-ups, dips and advanced skills like the one-arm push-up with structured bodyweight progressions.",
        "title": "BEST Calisthenics Coach Nairobi | Bodyweight Training, Push-up & Pull-up Programmes near me at D Dynamic Fitness",
        "meta": "Calisthenics coaching in Nairobi. Build real strength with bodyweight training, from your first full push-up to the one-arm push-up. Train with Don Michael Ondiro.",
        "h1": "Calisthenics Coach in Nairobi: Bodyweight Strength Training",
        "intro": [
            "Calisthenics is strength training with the one piece of equipment you always have: your own body. Done properly, it builds usable strength, better joint health and a physique that moves as good as it looks.",
            "On Instagram, Coach Don Michael Ondiro is known for his push-up challenges: one-arm push-ups on both sides, bare-knuckle push-ups and the 100-a-day habit. At D Dynamic Fitness he teaches you the progressions that get you there safely.",
        ],
        "sections": [
            ("Why calisthenics works", """
<p>Bodyweight training forces your whole body to work together. A strict push-up trains your chest, shoulders and triceps, but also your core, glutes and grip. Calisthenics athletes tend to be strong, lean and hard to injure.</p>
<ul>
<li><strong>Train anywhere:</strong> at home, in a park, on a rooftop or in the gym.</li>
<li><strong>No expensive equipment:</strong> a pull-up bar and a pair of parallettes go a long way.</li>
<li><strong>Clear milestones:</strong> every new skill is proof you are getting stronger.</li>
<li><strong>Joint-friendly:</strong> controlled bodyweight movement builds stable shoulders, wrists and hips.</li>
</ul>"""),
            ("Skill progressions we coach", """
<table>
<thead><tr><th>Skill</th><th>Starting point</th><th>Goal</th></tr></thead>
<tbody>
<tr><td>Push-up</td><td>Incline push-ups</td><td>Strict sets of 20+, then archer and one-arm push-ups</td></tr>
<tr><td>Pull-up</td><td>Scapular pulls and negatives</td><td>Strict pull-ups, then weighted and explosive variations</td></tr>
<tr><td>Dip</td><td>Bench dips and support holds</td><td>Full parallel bar dips</td></tr>
<tr><td>Core</td><td>Hollow body and plank holds</td><td>L-sit and hanging leg raises</td></tr>
<tr><td>Legs</td><td>Bodyweight squats and lunges</td><td>Pistol squats and shrimp squats</td></tr>
</tbody>
</table>"""),
            ("Repetition breeds mastery", """
<p>One of Don's training rules: use your space, anywhere and anytime, to get reps in. Calisthenics rewards frequent, high-quality practice more than occasional exhausting sessions. Your programme mixes coached sessions with short practice blocks you can do at home or at work.</p>
<p>Calisthenics also pairs well with <a href="{root}services/strength-conditioning.html">strength and conditioning</a> if you want to add weights, and with <a href="{root}services/mobility-flexibility.html">mobility training</a> if stiff shoulders or wrists are holding your skills back.</p>"""),
            ("Who calisthenics training is for", """
<ul>
<li>Beginners who cannot yet do a full push-up or pull-up.</li>
<li>Busy professionals who want effective workouts without a long gym commute.</li>
<li>Gym-goers who want to add real relative strength and control.</li>
<li>Martial artists and athletes who need strength without extra bulk.</li>
</ul>"""),
        ],
        "faqs": [
            ("Can I build muscle with calisthenics only?", "Yes. As long as exercises get progressively harder, bodyweight training builds muscle. We use tempo, leverage and harder variations to keep progressing."),
            ("I can't do a single push-up. Can I still start?", "Absolutely. Most clients start with incline push-ups and negatives. Following a structured progression, most beginners reach their first full push-up within a few weeks."),
            ("How long does it take to learn a one-arm push-up?", "It depends on your starting strength. Someone who can already do 25 strict push-ups might get there in a few months with consistent, coached progressions."),
            ("Do I need equipment for calisthenics?", "Not to start. A pull-up bar helps later, and sessions can run outdoors, at home or in a gym."),
        ],
    },
    {
        "slug": "jeet-kune-do-martial-arts",
        "name": "Jeet Kune Do & Martial Arts Fitness",
        "short": "Jeet Kune Do Training",
        "kw": "Jeet Kune Do Nairobi",
        "img": "kick",
        "blurb": "Learn Jeet Kune Do and MMA-style striking for self-defence, coordination and fight-ready conditioning.",
        "title": "BEST Jeet Kune Do Classes Nairobi | Martial Arts Fitness, MMA & Self-Defence Training near me at D Dynamic Fitness",
        "meta": "Jeet Kune Do and martial arts fitness training in Nairobi. Learn practical striking, kicks and self-defence while building fight-ready conditioning with coach Don.",
        "h1": "Jeet Kune Do & Martial Arts Training in Nairobi",
        "intro": [
            "Jeet Kune Do is the martial art and philosophy developed by Bruce Lee. It focuses on what works: direct strikes, efficient movement, and adapting to whatever is in front of you. It is one of the most practical systems you can learn for self-defence.",
            "Don Michael Ondiro trains in Jeet Kune Do and leisure MMA, and his students call him Sensei. At D Dynamic Fitness, martial arts training is about two things: learning skills you could really use, and getting fitter than you thought possible.",
        ],
        "sections": [
            ("What you will learn", """
<ul>
<li><strong>Stance and footwork:</strong> how to move, close distance and get out of range.</li>
<li><strong>Straight lead and combinations:</strong> the core Jeet Kune Do striking tools.</li>
<li><strong>Kicks:</strong> low-line kicks, front kicks and roundhouse kicks with proper chambering.</li>
<li><strong>Defence:</strong> parries, slips, blocks and simple counters.</li>
<li><strong>Pad and bag work:</strong> power, timing and accuracy against moving targets.</li>
<li><strong>Self-defence awareness:</strong> avoiding trouble first, and handling it if you cannot.</li>
</ul>"""),
            ("Martial arts conditioning", """
<p>Martial artists need a specific kind of fitness: explosive power, stamina across rounds and a strong core that links your legs to your hands. Sessions include the conditioning work you see on Don's Instagram, such as bare-knuckle push-ups, shadow boxing intervals and kick drills, scaled to your level.</p>
<p>If you want more striking volume, pair this with <a href="{root}services/boxing-kickboxing-fitness.html">boxing and kickboxing fitness</a>. If you want more raw strength, add <a href="{root}services/calisthenics-training.html">calisthenics training</a>.</p>"""),
            ("Is Jeet Kune Do right for you?", """
<table>
<thead><tr><th>You want to…</th><th>How the training helps</th></tr></thead>
<tbody>
<tr><td>Feel safer in the city</td><td>Practical self-defence and awareness skills</td></tr>
<tr><td>Get fit without boring cardio</td><td>Pad rounds and drills that burn a lot of energy</td></tr>
<tr><td>Improve coordination and focus</td><td>Footwork and combinations train mind and body together</td></tr>
<tr><td>Build discipline</td><td>Structured practice with clear progressions</td></tr>
</tbody>
</table>"""),
            ("Kids, teens and adults", """
<p>Martial arts training builds confidence and discipline at every age. Sessions are available for adults and, by arrangement, for teenagers and children, always focused on control, respect and safety. Ask on WhatsApp about private and small-group options.</p>"""),
        ],
        "faqs": [
            ("Do I need martial arts experience to start Jeet Kune Do?", "No. Beginners start with stance, footwork and basic strikes. Sessions are scaled to your fitness and experience."),
            ("Is there sparring?", "Sparring is optional and only introduced once you have the basics and want it. Many students train purely for fitness and self-defence skills."),
            ("What should I wear?", "Comfortable training clothes. Hand wraps and gloves are recommended once you start pad work. Ask in advance and we will advise what to buy."),
            ("Is Jeet Kune Do good for self-defence?", "Yes. Jeet Kune Do was designed to be practical and direct. Training covers awareness and avoidance as well as physical techniques."),
        ],
    },
    {
        "slug": "strength-conditioning",
        "name": "Strength & Performance Coaching",
        "short": "Strength & Conditioning",
        "kw": "strength and conditioning coach Nairobi",
        "img": "core",
        "blurb": "Athlete-style strength and conditioning for sport, performance and getting strong.",
        "title": "BEST Strength and Conditioning Coach Nairobi | Performance Training for Athletes & Sports Fitness near me at D Dynamic Fitness",
        "meta": "Strength and conditioning coach in Nairobi. Performance training for athletes, footballers and active adults: power, speed, strength and injury resilience.",
        "h1": "Strength & Conditioning Coach in Nairobi",
        "intro": [
            "Strength and conditioning is how athletes prepare their bodies for sport: more power, more speed, more endurance and fewer injuries. You do not need to be a professional athlete to benefit from training like one.",
            "Don Michael Ondiro is a certified fitness and performance coach. At D Dynamic Fitness, performance coaching combines barbell and dumbbell strength work, calisthenics, plyometrics and conditioning into one plan.",
        ],
        "sections": [
            ("What performance coaching covers", """
<ul>
<li><strong>Maximal strength:</strong> squats, deadlifts, presses and rows with sound technique.</li>
<li><strong>Power:</strong> jumps, throws and explosive bodyweight drills.</li>
<li><strong>Speed and agility:</strong> acceleration, change of direction and footwork.</li>
<li><strong>Conditioning:</strong> energy-system work matched to your sport.</li>
<li><strong>Injury resilience:</strong> mobility, single-leg strength and joint prep.</li>
</ul>"""),
            ("Who it is for", """
<table>
<thead><tr><th>Athlete</th><th>Training priority</th></tr></thead>
<tbody>
<tr><td>Footballers and rugby players</td><td>Sprint speed, power, repeat-effort conditioning</td></tr>
<tr><td>Runners</td><td>Leg strength, tendon resilience, running economy</td></tr>
<tr><td>Martial artists and boxers</td><td>Explosive power, core strength, round-to-round stamina</td></tr>
<tr><td>Active adults</td><td>Strength, energy and staying injury-free</td></tr>
</tbody>
</table>"""),
            ("How programmes are structured", """
<p>Training runs in blocks of four to six weeks. Each block has a clear focus, such as building a base, increasing strength or peaking for a season, and ends with a quick retest so you can see the progress in numbers.</p>
<p>Strength coaching pairs well with <a href="{root}services/mobility-flexibility.html">mobility and flexibility training</a> for recovery, and with <a href="{root}services/personal-training.html">one-on-one personal training</a> if you prefer every session fully coached.</p>"""),
        ],
        "faqs": [
            ("Do you train teams as well as individuals?", "Yes, by arrangement. Contact D Dynamic Fitness on WhatsApp to discuss team or small-group performance sessions."),
            ("Will strength training make me slower?", "No. Well-planned strength training makes athletes faster and more powerful. Programmes balance heavy work with speed and mobility."),
            ("Can I do this during my competitive season?", "Yes. In-season training is adjusted to maintain strength while keeping you fresh for matches and competitions."),
        ],
    },
    {
        "slug": "boxing-kickboxing-fitness",
        "name": "Boxing & Kickboxing Fitness",
        "short": "Boxing Fitness",
        "kw": "boxing trainer Nairobi",
        "img": "pads",
        "blurb": "High-energy pad work and striking drills that burn calories, relieve stress and sharpen your reflexes.",
        "title": "BEST Boxing Trainer Nairobi | Boxing & Kickboxing Fitness, Pad Work Sessions near me at D Dynamic Fitness",
        "meta": "Boxing and kickboxing fitness training in Nairobi. One-on-one pad work, striking technique and high-intensity conditioning with coach Don Michael Ondiro.",
        "h1": "Boxing & Kickboxing Fitness Trainer in Nairobi",
        "intro": [
            "Hitting pads burns a lot of energy. Boxing and kickboxing fitness sessions give you a full-body workout, stress relief and striking skills, all in under an hour.",
            "Pad work is a big part of how Don Michael Ondiro coaches. Holding pads lets him correct your technique in real time, set the pace and push you a little further each round.",
        ],
        "sections": [
            ("What a boxing fitness session includes", """
<ol>
<li><strong>Skipping and footwork warm-up</strong> to get your rhythm going.</li>
<li><strong>Technique rounds:</strong> jab, cross, hooks, uppercuts and kicks.</li>
<li><strong>Pad work rounds</strong> with your coach calling combinations.</li>
<li><strong>Conditioning:</strong> shadow boxing intervals, push-ups and core work.</li>
<li><strong>Cool-down</strong> and mobility for shoulders and hips.</li>
</ol>"""),
            ("Benefits", """
<ul>
<li>Burns a high number of calories per session.</li>
<li>Builds shoulder, arm and core strength.</li>
<li>Improves hand-eye coordination and reaction time.</li>
<li>Reduces stress, especially after a long day in traffic.</li>
<li>Teaches basic striking you can use for self-defence.</li>
</ul>
<p>Want to go deeper into martial arts? Move on to <a href="{root}services/jeet-kune-do-martial-arts.html">Jeet Kune Do training</a>. Want more general strength? Combine boxing with <a href="{root}services/personal-training.html">personal training</a>.</p>"""),
        ],
        "faqs": [
            ("Do I get hit in boxing fitness sessions?", "No. Boxing fitness is non-contact. You strike pads and bags, not people."),
            ("Is boxing fitness good for weight loss?", "Yes. Pad rounds are high-intensity interval training, which makes them very effective for burning calories alongside a sensible diet."),
            ("Do I need my own gloves?", "Bring your own if you have them. If you don't, ask before your first session and we will advise."),
        ],
    },
    {
        "slug": "mobility-flexibility",
        "name": "Mobility & Flexibility Training",
        "short": "Mobility Training",
        "kw": "mobility training Nairobi",
        "img": "mobility",
        "blurb": "Loosen stiff hips, shoulders and backs so you can train harder, sit better and move without pain.",
        "title": "BEST Mobility Training Nairobi | Flexibility, Stretching & Posture Coaching near me at D Dynamic Fitness",
        "meta": "Mobility and flexibility training in Nairobi. Fix stiff shoulders, hips and back, improve posture and move better with guided sessions from coach Don.",
        "h1": "Mobility & Flexibility Training in Nairobi",
        "intro": [
            "Long hours at a desk and in traffic leave most people stiff in the same places: hips, upper back and shoulders. Mobility training restores that range of motion, so you can train harder, sit better and move without aches.",
            "At D Dynamic Fitness, mobility is part of every programme. Stick drills, controlled joint rotations and loaded stretching are the same tools Don uses to keep his own martial arts and calisthenics training pain-free.",
        ],
        "sections": [
            ("What mobility training targets", """
<table>
<thead><tr><th>Area</th><th>Common problem</th><th>What we work on</th></tr></thead>
<tbody>
<tr><td>Shoulders</td><td>Rounded posture, overhead stiffness</td><td>Stick dislocates, thoracic rotation, scapular control</td></tr>
<tr><td>Hips</td><td>Tight from sitting</td><td>Hip flexor and adductor mobility, 90/90 drills</td></tr>
<tr><td>Lower back</td><td>Aches after long days</td><td>Core control, hamstring and glute mobility</td></tr>
<tr><td>Ankles</td><td>Poor squat depth</td><td>Ankle dorsiflexion and calf work</td></tr>
</tbody>
</table>"""),
            ("Mobility versus stretching", """
<p>Stretching makes a muscle longer for a moment. Mobility training teaches your body to control that new range, which is why the results last. Sessions combine both, with an emphasis on active control.</p>
<p>Mobility work makes every other service work better, especially <a href="{root}services/calisthenics-training.html">calisthenics</a> and <a href="{root}services/strength-conditioning.html">strength and conditioning</a>.</p>"""),
        ],
        "faqs": [
            ("How often should I do mobility training?", "Short daily sessions of 10 to 15 minutes give the best results. Your coach will give you a routine to do between sessions."),
            ("Can mobility training help back pain?", "It often helps with general stiffness and aches from sitting. For pain from a specific injury, see a medical professional first and we will work alongside their advice."),
            ("Is mobility training suitable for older adults?", "Yes. Mobility work is low-impact and scaled to each person, so it suits any age."),
        ],
    },
]

# ---------------------------------------------------------------- areas
AREAS = [
    {
        "slug": "westlands",
        "name": "Westlands",
        "landmarks": "Sarit Centre, Westgate, The Mall and Waiyaki Way",
        "intro": "Westlands moves fast. Between offices on Waiyaki Way, meetings at Sarit Centre and evenings out, finding time to train properly is the hard part. D Dynamic Fitness helps Westlands professionals fit focused, results-driven sessions into packed schedules.",
        "local": "Many Westlands clients train early, before the Waiyaki Way traffic builds, or straight after work. Short, high-intensity sessions such as calisthenics circuits and boxing pad rounds work well when you only have 45 minutes.",
        "services": ["personal-training", "boxing-kickboxing-fitness", "calisthenics-training"],
        "faqs": [
            ("Do you offer early-morning training for Westlands clients?", "Yes. Early sessions are popular with Westlands professionals who want to train before work. Message on WhatsApp to check available times."),
            ("Can we train near my office in Westlands?", "Possibly. Contact D Dynamic Fitness with your location and we will confirm the best training option for you."),
        ],
    },
    {
        "slug": "kilimani",
        "name": "Kilimani",
        "landmarks": "Yaya Centre, Prestige Plaza, Argwings Kodhek Road and Ngong Road",
        "intro": "Kilimani is one of Nairobi's busiest residential neighbourhoods, full of apartments, young professionals and families. D Dynamic Fitness offers Kilimani residents coaching that works around apartment life and busy weeks.",
        "local": "A lot of Kilimani residents live in apartments with small gyms or rooftop space. Calisthenics suits that well. All you need is a bit of floor, a bar and a coach who knows how to make it hard.",
        "services": ["calisthenics-training", "personal-training", "mobility-flexibility"],
        "faqs": [
            ("Can I train in my Kilimani apartment gym?", "Many apartment gyms work well for coached sessions. Share your location and set-up on WhatsApp and we will advise."),
            ("Do you do rooftop or outdoor sessions?", "Bodyweight and boxing sessions can run outdoors when space allows. Ask about options for your building."),
        ],
    },
    {
        "slug": "kileleshwa",
        "name": "Kileleshwa",
        "landmarks": "Othaya Road, Kasuku Centre and the Kileleshwa ring road",
        "intro": "Leafy, quiet and close to everything, Kileleshwa is a great place to build a training habit. D Dynamic Fitness works with Kileleshwa clients who want steady, coached progress without the crowds of a big commercial gym.",
        "local": "Kileleshwa's quieter streets suit early runs and outdoor conditioning. We combine those with coached strength and martial arts sessions so your week has structure.",
        "services": ["strength-conditioning", "jeet-kune-do-martial-arts", "personal-training"],
        "faqs": [
            ("Do you train families in Kileleshwa?", "Yes. Family and small-group sessions, including martial arts for teens and kids, are available by arrangement."),
            ("How far in advance should I book?", "Popular morning and evening slots fill up, so message a few days ahead where possible."),
        ],
    },
    {
        "slug": "lavington",
        "name": "Lavington",
        "landmarks": "Lavington Mall, Valley Arcade and James Gichuru Road",
        "intro": "Lavington clients usually want one thing from a coach: real, measurable results with a professional who turns up prepared. D Dynamic Fitness delivers structured one-on-one coaching for Lavington residents of every fitness level.",
        "local": "Many Lavington clients prefer private sessions where the whole hour is about them. One-on-one training, mobility work for desk-bound backs and Jeet Kune Do for self-defence are the most requested services in the area.",
        "services": ["personal-training", "mobility-flexibility", "jeet-kune-do-martial-arts"],
        "faqs": [
            ("Do you offer home personal training in Lavington?", "Ask on WhatsApp with your location and we will confirm whether home sessions are available for your area."),
            ("Can older adults train with you?", "Yes. Programmes are scaled to each person, with a strong focus on mobility, balance and safe strength."),
        ],
    },
    {
        "slug": "karen",
        "name": "Karen",
        "landmarks": "Karen Hub, The Waterfront, Karen Blixen Museum and Ngong Road Forest",
        "intro": "With green space, forest trails and plenty of room, Karen suits an active lifestyle. D Dynamic Fitness coaches Karen residents who want to make the most of it, from athletes and runners to families and beginners.",
        "local": "Karen's open spaces and the trails near Ngong Road Forest work well for outdoor conditioning. We pair that with strength and performance work so runners, cyclists and weekend athletes stay strong and injury-free.",
        "services": ["strength-conditioning", "boxing-kickboxing-fitness", "calisthenics-training"],
        "faqs": [
            ("Do you coach runners and cyclists in Karen?", "Yes. Strength and conditioning for endurance athletes, including leg strength and injury prevention, is a core service."),
            ("Can sessions be held outdoors in Karen?", "Outdoor sessions are possible depending on location and weather. Ask on WhatsApp to arrange."),
        ],
    },
    {
        "slug": "parklands",
        "name": "Parklands",
        "landmarks": "City Park, Limuru Road, Aga Khan University Hospital and the Parklands avenues",
        "intro": "Parklands is close to the CBD and Westlands, with a busy mix of families, students and professionals. D Dynamic Fitness brings structured coaching to Parklands residents who want to get stronger, fitter and more confident.",
        "local": "Students and young professionals in Parklands often want efficient, affordable training they can keep up. Calisthenics and boxing fitness build strength and stamina with minimal equipment.",
        "services": ["calisthenics-training", "boxing-kickboxing-fitness", "jeet-kune-do-martial-arts"],
        "faqs": [
            ("Do you offer small-group sessions in Parklands?", "Yes. Training with a friend or a small group is a great way to share the cost and stay motivated. Ask about group options."),
            ("Is martial arts training available for students?", "Yes. Jeet Kune Do and boxing fitness are popular with students looking for fitness and self-defence skills."),
        ],
    },
]

# ---------------------------------------------------------------- general FAQs
FAQS = [
    ("Who is the coach at D Dynamic Fitness?", "D Dynamic Fitness is run by Don Michael Ondiro, a certified fitness and performance coach in Nairobi who also trains in Jeet Kune Do and MMA. He holds a BA in Economics."),
    ("Where in Nairobi do you train clients?", "D Dynamic Fitness works with clients across Nairobi, including Westlands, Kilimani, Kileleshwa, Lavington, Karen and Parklands. Message on WhatsApp with your location to confirm."),
    ("What services do you offer?", "One-on-one personal training, fitness and weight training, MMA training, aerobics and cardio classes, Jeet Kune Do, boxing and kickboxing fitness, calisthenics, weight loss coaching, strength and conditioning, group and partner classes, kids and teens fitness, and mobility training."),
    ("I'm a complete beginner. Is that okay?", "Yes. Every programme starts with an assessment and is built from your current fitness level. Beginners are very welcome."),
    ("How do I book a session?", "Tap the WhatsApp or Call button on any page, or use the contact form. Tell us your goal, location and preferred times, and we will reply to arrange your first session."),
    ("Do you offer online coaching?", "Ask on WhatsApp about remote programmes and check-ins if you can't train in person."),
    ("What should I bring to my first session?", "Comfortable training clothes, trainers, a water bottle and a towel. For boxing or martial arts, bring hand wraps if you have them."),
    ("How much does training cost?", "Rates depend on the service, number of sessions and location. Contact D Dynamic Fitness for current prices and package options."),
]
