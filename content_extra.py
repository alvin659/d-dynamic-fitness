# Extra long-form sections (playbook "advanced" step: build topical and local authority).
# build.py appends these to the matching service / area pages. {root} is replaced with the
# relative path to the site root.

SERVICE_EXTRA = {
    "personal-training": {
        "sections": [
            ("Your first four weeks", """
<p>The first month sets the tone for everything that follows, so it is planned carefully. Most new clients follow this pattern.</p>
<table>
<thead><tr><th>Week</th><th>Focus</th><th>What you will notice</th></tr></thead>
<tbody>
<tr><td>1</td><td>Assessment, technique basics, building the habit</td><td>Some muscle soreness, a clear plan and a routine that fits your week</td></tr>
<tr><td>2</td><td>Learning the main movement patterns properly</td><td>Exercises start to feel smoother and more controlled</td></tr>
<tr><td>3</td><td>First real progressions: more weight, reps or harder variations</td><td>Better energy and sleep, and your first strength gains</td></tr>
<tr><td>4</td><td>Check-in and retest</td><td>Measurable progress you can see in your numbers</td></tr>
</tbody>
</table>
<p>After week four, your programme is updated based on what the retest shows. That cycle of train, test and adjust is what keeps progress going long after the beginner gains slow down.</p>"""),
            ("Training around your schedule", """
<p>Training in Nairobi comes with its own challenges: unpredictable traffic, long working days and weekends full of family and church commitments. A good programme accepts that reality instead of pretending it does not exist.</p>
<ul>
<li><strong>Flexible timing:</strong> early-morning sessions beat the traffic, and evening slots suit people who cannot train before work.</li>
<li><strong>Short-session backups:</strong> if a meeting runs late, you get a 20-minute version of the workout so the week is not lost.</li>
<li><strong>Travel plans:</strong> heading upcountry or out of town? You get a bodyweight plan you can do in a hotel room or a compound.</li>
<li><strong>Realistic nutrition:</strong> ugali, githeri, sukuma, chapati, nyama choma. You do not have to give up the food you love. You learn how much of it fits your goal.</li>
</ul>"""),
            ("Nutrition guidance", """
<p>You cannot out-train a diet that works against you, but you also do not need expensive supplements or imported meal plans. Nutrition coaching covers five basics:</p>
<ol>
<li><strong>Protein at every meal:</strong> eggs, beans, ndengu, fish, chicken, beef or milk.</li>
<li><strong>Plenty of vegetables:</strong> sukuma wiki, cabbage, spinach, tomatoes and whatever is in season at the market.</li>
<li><strong>Portion control for starches:</strong> ugali, rice and chapati are fine, in amounts that match your goal.</li>
<li><strong>Water first:</strong> most people are under-hydrated, especially in the dry season.</li>
<li><strong>Consistency over perfection:</strong> a good week beats a perfect day followed by giving up.</li>
</ol>
<p>Want to go beyond the basics? Pair personal training with <a href="{root}services/calisthenics-training.html">calisthenics coaching</a> to build relative strength, or <a href="{root}services/boxing-kickboxing-fitness.html">boxing fitness</a> for high-energy conditioning.</p>"""),
            ("Checklist: getting the most from personal training", """
<ul class="ticks">
<li>Tell your coach about any injuries, conditions or medication before your first session.</li>
<li>Sleep seven to eight hours where possible. Recovery is where the progress happens.</li>
<li>Eat a light meal one to two hours before training.</li>
<li>Log your sessions so you can see your progress over months.</li>
<li>Do the short homework sessions between coached workouts.</li>
<li>Be honest at check-ins. Your plan can only adapt to what your coach knows.</li>
</ul>"""),
        ],
        "faqs": [
            ("Is personal training suitable if I have an old injury?", "Often, yes. Tell your coach about any injury at the assessment. Programmes avoid aggravating movements and build strength around the problem area. For recent or serious injuries, get medical clearance first."),
            ("Can I train with a friend or partner?", "Yes. Partner sessions share the cost and keep you both accountable. Ask on WhatsApp about shared session rates."),
        ],
    },
    "calisthenics-training": {
        "sections": [
            ("A sample beginner calisthenics week", """
<p>This is the kind of structure a beginner might follow in their first month. Your real programme is adjusted to your starting level.</p>
<table>
<thead><tr><th>Day</th><th>Session</th><th>Key exercises</th></tr></thead>
<tbody>
<tr><td>Monday</td><td>Push (coached)</td><td>Incline push-ups, pike push-ups, bench dips, plank</td></tr>
<tr><td>Tuesday</td><td>Practice block (10 min)</td><td>Push-up negatives and a hollow body hold</td></tr>
<tr><td>Wednesday</td><td>Pull and legs (coached)</td><td>Australian rows, scapular pulls, squats, lunges</td></tr>
<tr><td>Thursday</td><td>Mobility (15 min)</td><td>Wrist prep, shoulder stick drills, hip openers</td></tr>
<tr><td>Friday</td><td>Full body (coached)</td><td>Push-up and row supersets, glute bridges, core circuit</td></tr>
<tr><td>Weekend</td><td>Active rest</td><td>A walk, a run, play or a 100 push-up challenge spread through the day</td></tr>
</tbody>
</table>"""),
            ("The three rules of progression", """
<p>Calisthenics does not use heavier plates to get harder, so progress comes from three main levers. Understanding them is what separates people who stall at 20 push-ups from people who reach the one-arm push-up.</p>
<ol>
<li><strong>Leverage:</strong> moving your body to a less helpful angle, for example from incline to flat to decline push-ups, or from knee raises to straight-leg raises.</li>
<li><strong>Range and control:</strong> deeper reps, slower lowering phases and pauses at the hardest point.</li>
<li><strong>Load distribution:</strong> shifting more weight onto one arm or leg, as in archer push-ups, assisted one-arm work and pistol squats.</li>
</ol>
<p>Each skill in your programme has a ladder of progressions. You only move up a rung once you own the current one, with clean form, for the target reps.</p>"""),
            ("Common calisthenics mistakes we fix", """
<ul>
<li><strong>Sagging hips in push-ups:</strong> fixed with plank work and glute engagement cues.</li>
<li><strong>Kipping before strict strength:</strong> we build strict pull-ups first, because they protect your shoulders.</li>
<li><strong>Skipping wrist preparation:</strong> wrists take a lot of load in bodyweight training, so they get their own warm-up.</li>
<li><strong>Chasing skills too early:</strong> a one-arm push-up needs a strong base of full push-ups, archer push-ups and core control.</li>
<li><strong>Training to failure every set:</strong> quality reps with a little left in the tank build strength faster and more safely.</li>
</ul>"""),
            ("Calisthenics in Nairobi: where to train", """
<p>One of the best things about calisthenics is that Nairobi itself becomes your gym. Clients train in apartment gyms, on rooftops, in compounds and in public spaces with bars and benches. Coach Don films many of his own challenges outdoors for exactly that reason: you do not need a fancy facility to get strong.</p>
<p>We coach calisthenics clients across the city, including <a href="{root}areas/kilimani.html">Kilimani</a> and <a href="{root}areas/parklands.html">Parklands</a>, where apartment living makes bodyweight training a good option.</p>"""),
        ],
        "faqs": [
            ("Is calisthenics better than lifting weights?", "Neither is better for everyone. Calisthenics builds excellent relative strength and control, and weights make it easy to add load. Many clients combine both."),
            ("Is calisthenics safe for my joints?", "Yes, when progressions are followed and joints are prepared properly. Wrist and shoulder warm-ups are built into every session."),
        ],
    },
    "jeet-kune-do-martial-arts": {
        "sections": [
            ("The principles behind Jeet Kune Do", """
<p>Jeet Kune Do translates roughly as "the way of the intercepting fist". Rather than a fixed set of forms, it is a set of principles. These ideas shape how every class is taught:</p>
<ul>
<li><strong>Economy of motion:</strong> the shortest, most direct path to the target wins.</li>
<li><strong>Interception:</strong> meet an attack as it starts instead of waiting to block it.</li>
<li><strong>Simplicity:</strong> a small set of techniques trained well beats a large set trained badly.</li>
<li><strong>Adaptability:</strong> absorb what is useful, discard what is not, and adapt to your own body.</li>
<li><strong>Live training:</strong> skills are tested against moving, resisting partners and pads, as well as in the air.</li>
</ul>"""),
            ("Your progression path", """
<table>
<thead><tr><th>Stage</th><th>Focus</th><th>Typical timeframe</th></tr></thead>
<tbody>
<tr><td>Foundation</td><td>Stance, footwork, straight lead, basic kicks, guard</td><td>First 1 to 2 months</td></tr>
<tr><td>Development</td><td>Combinations, defence and counters, pad work at pace</td><td>Months 2 to 6</td></tr>
<tr><td>Application</td><td>Timing drills, controlled partner work, self-defence scenarios</td><td>Months 6+</td></tr>
<tr><td>Ongoing</td><td>Refining your own style, conditioning, optional light sparring</td><td>As far as you want to go</td></tr>
</tbody>
</table>
<p>Timeframes depend on how often you train. Two sessions a week plus a little shadow boxing at home is enough for steady progress.</p>"""),
            ("A typical martial arts session", """
<ol>
<li><strong>Warm-up:</strong> skipping, joint mobility and dynamic stretches for hips and shoulders.</li>
<li><strong>Footwork drills:</strong> advancing, retreating, angling off and changing range.</li>
<li><strong>Technique block:</strong> one or two new skills broken down step by step.</li>
<li><strong>Pad rounds:</strong> putting the skill together at speed, with power and timing.</li>
<li><strong>Conditioning:</strong> push-up variations, core work and short intervals.</li>
<li><strong>Cool-down:</strong> stretching and a quick review of what you learned.</li>
</ol>"""),
            ("Self-defence in the city", """
<p>Self-defence starts before any technique. Training covers awareness on busy streets and matatu stages, keeping distance, confident body language and de-escalation, because avoiding a fight is always the first option. Physical skills are taught as a last resort, built on simple, high-percentage strikes and escapes.</p>
<p>Martial arts training is popular with clients in <a href="{root}areas/kileleshwa.html">Kileleshwa</a> and <a href="{root}areas/lavington.html">Lavington</a>, including families looking for confidence-building classes for teenagers. Students who want a stronger base can add <a href="{root}services/strength-conditioning.html">strength and conditioning</a>.</p>"""),
        ],
        "faqs": [
            ("How is Jeet Kune Do different from karate or taekwondo?", "Jeet Kune Do has no fixed forms or belt system in the traditional sense. It focuses on direct, practical techniques, footwork and adapting to the situation."),
            ("Am I too old to start martial arts?", "No. Training is scaled to your age, fitness and goals. Many adults start in their 30s, 40s and beyond, mainly for fitness and confidence."),
        ],
    },
    "strength-conditioning": {
        "sections": [
            ("The building blocks of athletic performance", """
<p>Every sport demands a different mix of qualities, but all of them sit on the same foundation. Performance coaching works on each layer in order:</p>
<ol>
<li><strong>Movement quality:</strong> squat, hinge, lunge, push, pull and carry patterns done well.</li>
<li><strong>Strength:</strong> the ability to produce force, the base for everything else.</li>
<li><strong>Power:</strong> producing that force quickly, for jumping, sprinting, striking and throwing.</li>
<li><strong>Speed and agility:</strong> applying power in the right direction at the right time.</li>
<li><strong>Sport-specific conditioning:</strong> fitness that matches the demands of your game.</li>
</ol>
<p>Skipping steps is the most common reason athletes get injured. A footballer chasing sprint speed without single-leg strength is a hamstring injury waiting to happen.</p>"""),
            ("Sample training block for a footballer", """
<table>
<thead><tr><th>Session</th><th>Main work</th><th>Supporting work</th></tr></thead>
<tbody>
<tr><td>Strength A</td><td>Squats, Romanian deadlifts</td><td>Copenhagen planks, Nordic hamstring curls</td></tr>
<tr><td>Speed and power</td><td>Acceleration sprints, box jumps, bounds</td><td>Ankle and calf work, core anti-rotation</td></tr>
<tr><td>Strength B</td><td>Split squats, push-ups or presses, rows</td><td>Hip mobility, single-leg balance</td></tr>
<tr><td>Conditioning</td><td>Repeat sprint intervals</td><td>Mobility and recovery</td></tr>
</tbody>
</table>
<p>The same structure adapts for rugby players, basketball players, runners and martial artists by changing the exercise selection and the conditioning work.</p>"""),
            ("Testing and tracking", """
<p>At the start and end of each block we test a few simple markers, chosen for your sport:</p>
<ul>
<li>Strength: rep maximums on key lifts or strict pull-ups and push-ups.</li>
<li>Power: broad jump or vertical jump.</li>
<li>Speed: 10 m and 20 m sprint times.</li>
<li>Conditioning: a repeat-effort test matched to your sport.</li>
<li>Mobility: simple range-of-motion screens for hips, ankles and shoulders.</li>
</ul>"""),
            ("Recovery matters as much as training", """
<p>Strength is built in training but gained during recovery. Programmes include guidance on sleep, hydration, eating enough protein and planning lighter weeks. If you play matches on the weekend, heavy sessions are scheduled early in the week so you arrive fresh.</p>
<p>Performance coaching is popular with runners, cyclists and weekend athletes in <a href="{root}areas/karen.html">Karen</a> and <a href="{root}areas/kileleshwa.html">Kileleshwa</a>. For extra striking power, combine it with <a href="{root}services/jeet-kune-do-martial-arts.html">Jeet Kune Do</a> or <a href="{root}services/boxing-kickboxing-fitness.html">boxing fitness</a>.</p>"""),
        ],
        "faqs": [
            ("At what age can young athletes start strength training?", "Supervised, technique-focused strength training is suitable for teenagers. The emphasis is on movement quality and bodyweight skills before heavy loads."),
            ("How many sessions a week do athletes need?", "Two to three strength and conditioning sessions a week is typical, depending on your sport's training and match schedule."),
        ],
    },
    "boxing-kickboxing-fitness": {
        "sections": [
            ("Why pad work is different from a bag", """
<p>A heavy bag just hangs there. A coach holding pads moves, angles, calls combinations and occasionally fires back a slow tap to test your guard. That makes pad work far better for timing, accuracy and reaction speed. It also lets your coach fix your technique in real time, which is the fastest way to improve.</p>
<ul>
<li><strong>Moving targets</strong> train footwork and distance management.</li>
<li><strong>Called combinations</strong> train your brain as well as your body.</li>
<li><strong>Instant feedback</strong> on hand position, hip rotation and balance.</li>
<li><strong>Controlled intensity:</strong> your coach sets the pace to match your fitness.</li>
</ul>"""),
            ("Core boxing and kickboxing techniques", """
<table>
<thead><tr><th>Technique</th><th>What it is</th><th>Why it matters</th></tr></thead>
<tbody>
<tr><td>Jab</td><td>Fast straight punch with the lead hand</td><td>Measures distance and sets up everything else</td></tr>
<tr><td>Cross</td><td>Powerful straight punch with the rear hand</td><td>Main power punch, driven by the hips</td></tr>
<tr><td>Hook</td><td>Short curved punch to the side</td><td>Close-range power from rotation</td></tr>
<tr><td>Uppercut</td><td>Rising punch from below</td><td>Breaks through a tight guard</td></tr>
<tr><td>Roundhouse kick</td><td>Circular kick with the shin</td><td>Kickboxing's main power kick</td></tr>
<tr><td>Front kick (teep)</td><td>Straight push kick</td><td>Controls distance and stops forward pressure</td></tr>
</tbody>
</table>"""),
            ("A sample 45-minute session", """
<ol>
<li><strong>5 minutes:</strong> skipping and shadow boxing to warm up.</li>
<li><strong>10 minutes:</strong> technique drill on one or two punches or kicks.</li>
<li><strong>18 minutes:</strong> six rounds of pad work (2 minutes on, 1 minute rest).</li>
<li><strong>8 minutes:</strong> conditioning finisher, for example bare-knuckle push-ups, sit-ups and burpees.</li>
<li><strong>4 minutes:</strong> stretching for shoulders, hips and calves.</li>
</ol>"""),
            ("Boxing fitness for stress relief", """
<p>A hard set of pad rounds after work clears your head. Boxing fitness combines focus and physical effort, which makes it a favourite with busy professionals in <a href="{root}areas/westlands.html">Westlands</a>. It is also popular with students in <a href="{root}areas/parklands.html">Parklands</a> who want fitness and basic self-defence in one session.</p>
<p>If you enjoy striking and want to go deeper into technique and self-defence, the natural next step is <a href="{root}services/jeet-kune-do-martial-arts.html">Jeet Kune Do training</a>.</p>"""),
            ("What to bring", """
<ul class="ticks">
<li>Hand wraps (essential once you start hitting pads)</li>
<li>Boxing gloves (12 to 14 oz suits most adults)</li>
<li>Comfortable clothes you can move and sweat in</li>
<li>Water bottle and a small towel</li>
<li>Trainers with good grip, or barefoot for kickboxing on mats</li>
</ul>"""),
        ],
        "faqs": [
            ("Is boxing fitness suitable for women?", "Absolutely. Boxing fitness is non-contact and scaled to each person. Many women train for fitness, confidence and self-defence skills."),
            ("How quickly will I see results from boxing fitness?", "Most people notice better stamina within two to three weeks of consistent sessions, with body composition changes following when combined with sensible eating."),
            ("Can I combine boxing with weight training?", "Yes. Boxing pairs well with strength training. Your coach can plan both so you recover properly between sessions."),
        ],
    },
    "mobility-flexibility": {
        "sections": [
            ("Signs you need mobility work", """
<ul>
<li>You cannot squat to parallel without your heels lifting or your back rounding.</li>
<li>Reaching overhead makes your lower back arch or your shoulders pinch.</li>
<li>You feel stiff for the first hour after waking up.</li>
<li>Your hips feel tight after long drives or hours at a desk.</li>
<li>Old injuries flare up when you increase training.</li>
<li>Your calisthenics or lifting progress has stalled because of positions you cannot reach.</li>
</ul>"""),
            ("A 10-minute daily mobility routine", """
<p>This simple routine is a starting point many clients use between coached sessions. Move slowly and stay within a comfortable range.</p>
<ol>
<li><strong>Neck and shoulder circles:</strong> 1 minute.</li>
<li><strong>Cat-cow:</strong> 10 slow reps to mobilise the spine.</li>
<li><strong>Thoracic rotations on all fours:</strong> 8 reps per side.</li>
<li><strong>Stick shoulder dislocates:</strong> 10 slow reps with a broomstick or training stick, hands wide.</li>
<li><strong>90/90 hip switches:</strong> 8 reps per side.</li>
<li><strong>Deep squat hold:</strong> 1 minute, holding onto something for support if needed.</li>
<li><strong>Kneeling hip flexor stretch:</strong> 45 seconds per side.</li>
<li><strong>Wall ankle mobilisations:</strong> 10 reps per side.</li>
</ol>
<p>Your coach will adjust the routine for your specific problem areas after your assessment.</p>"""),
            ("Mobility for desk workers", """
<p>Many Nairobi professionals spend eight or more hours a day sitting, plus time in traffic on Mombasa Road, Waiyaki Way or Ngong Road. Sitting is not the enemy, but staying still for hours is. Mobility coaching gives you:</p>
<ul>
<li>Quick desk-friendly movements you can do between meetings.</li>
<li>Posture strategies that do not rely on sitting perfectly straight all day.</li>
<li>Strengthening for the muscles that switch off with long sitting: glutes, upper back and deep core.</li>
</ul>
<p>Desk-worker mobility programmes are popular with clients in <a href="{root}areas/lavington.html">Lavington</a> and <a href="{root}areas/kilimani.html">Kilimani</a>. For a complete plan, combine mobility with <a href="{root}services/personal-training.html">one-on-one personal training</a>.</p>"""),
            ("Mobility for martial artists and athletes", """
<p>High kicks need open hips. Strong punches need a mobile upper back. Deep squats need good ankles. Mobility work is built into Coach Don's own Jeet Kune Do and calisthenics training, and it is part of every athlete's programme at D Dynamic Fitness, so you can reach the positions your sport demands without forcing them.</p>"""),
        ],
        "faqs": [
            ("Will mobility training make me more flexible for kicks?", "Yes. Active hip mobility and controlled stretching improve kicking height and reduce strain on the hips and lower back."),
            ("Do I need any equipment for mobility training?", "Very little. A mat, a broomstick or training stick and a resistance band cover most of what you need."),
        ],
    },
}

AREA_EXTRA = {
    "westlands": {
        "sections": [
            ("Who we train in Westlands", """
<p>Our Westlands clients include bankers, tech workers, consultants, NGO staff and entrepreneurs who spend long days around Waiyaki Way, Woodvale Grove and the office parks along Chiromo Road. Most are short on time and want a coach who makes every minute count.</p>
<ul>
<li><strong>Before-work sessions</strong> for people who want training done before the day takes over.</li>
<li><strong>Lunchtime express sessions</strong> of 30 to 40 minutes for those working nearby.</li>
<li><strong>After-work boxing rounds</strong> to burn off the stress of the day.</li>
</ul>"""),
            ("Beat the Waiyaki Way traffic", """
<p>Anyone who commutes through Westlands knows that traffic can wreck an evening workout plan. Training early, before roads around the Westlands roundabout and Mpaka Road fill up, is the most reliable way to stay consistent. If you train in the evening, scheduling a little later, once the rush has eased, often works better than fighting the jam.</p>"""),
            ("A training week for a busy Westlands professional", """
<table>
<thead><tr><th>Day</th><th>Session</th><th>Length</th></tr></thead>
<tbody>
<tr><td>Monday</td><td>Coached strength session</td><td>45 min</td></tr>
<tr><td>Wednesday</td><td>Boxing pad rounds and conditioning</td><td>45 min</td></tr>
<tr><td>Friday</td><td>Calisthenics and mobility</td><td>45 min</td></tr>
<tr><td>Other days</td><td>10-minute mobility or push-up practice at home</td><td>10 min</td></tr>
</tbody>
</table>
<p>Three focused sessions a week, plus short practice blocks, is enough for real change even with a demanding job.</p>"""),
            ("Tips for staying fit in Westlands", """
<ul class="ticks">
<li>Use the stairs in your office block instead of the lift.</li>
<li>Plan your after-work social plans around training days, not the other way round.</li>
<li>Pack a gym bag the night before early sessions.</li>
<li>Choose grilled options when eating out at Westlands restaurants.</li>
</ul>"""),
        ],
        "faqs": [
            ("Do you offer lunchtime sessions in Westlands?", "Shorter lunchtime sessions can be arranged depending on availability and location. Ask on WhatsApp."),
            ("Can my colleagues and I train as a group?", "Yes. Small-group and corporate sessions are a great option for teams. Contact us to discuss."),
        ],
    },
    "kilimani": {
        "sections": [
            ("Who we train in Kilimani", """
<p>Kilimani's mix of apartments along Argwings Kodhek Road, Lenana Road and the streets around Yaya Centre makes it home to young professionals, couples, families and plenty of people who work from home. Clients here often want flexible training that fits around hybrid work and busy social lives.</p>
<ul>
<li><strong>Remote workers</strong> who need a reason to get out of the chair.</li>
<li><strong>Couples</strong> who train together to share the cost and motivation.</li>
<li><strong>Beginners</strong> who want a patient coach rather than a crowded gym.</li>
</ul>"""),
            ("Making the most of apartment gyms and rooftops", """
<p>Many Kilimani buildings have a small gym or rooftop space with a few dumbbells, a bench and maybe a pull-up bar. That is more than enough. Coach Don's own Instagram is full of workouts done on rooftops and in simple spaces: one-arm push-ups, bare-knuckle push-ups and shadow boxing. A good coach turns limited equipment into a hard, effective session.</p>
<table>
<thead><tr><th>Equipment available</th><th>What we can train</th></tr></thead>
<tbody>
<tr><td>Floor space only</td><td>Calisthenics, boxing drills, mobility, core</td></tr>
<tr><td>Dumbbells and a bench</td><td>Full strength programme for most goals</td></tr>
<tr><td>Pull-up bar</td><td>Pull-up progressions, hanging core work</td></tr>
<tr><td>Rooftop or open area</td><td>Sprints, shadow boxing, pad work</td></tr>
</tbody>
</table>"""),
            ("Working from home? Move more", """
<p>If you work from a Kilimani apartment, the biggest health risk is not missing the gym. It is sitting for 10 hours straight. Alongside coached sessions, clients get simple rules: stand up every 45 minutes, take a walk around the block at lunch, and do a short mobility routine before and after the working day. See our <a href="{root}services/mobility-flexibility.html">mobility training</a> page for more.</p>"""),
            ("Tips for staying fit in Kilimani", """
<ul class="ticks">
<li>Walk to nearby errands at Yaya Centre or Prestige Plaza instead of taking a cab for short trips.</li>
<li>Book a regular weekly slot with your coach so training becomes non-negotiable.</li>
<li>Use your building's stairs for quick conditioning finishers.</li>
<li>Stock your kitchen with easy protein: eggs, yoghurt, beans and ndengu.</li>
</ul>"""),
        ],
        "faqs": [
            ("Can couples train together in Kilimani?", "Yes. Partner sessions are popular and share the cost. Programmes can be adjusted for two different fitness levels."),
            ("Is there a minimum number of sessions?", "Ask on WhatsApp for current options. Most clients book a regular weekly schedule for the best results."),
        ],
    },
    "kileleshwa": {
        "sections": [
            ("Who we train in Kileleshwa", """
<p>Kileleshwa is a residential favourite for families and professionals, with tree-lined streets around Othaya Road, Gatundu Road and Laikipia Road. Clients here tend to want a long-term training relationship: steady progress, consistent scheduling and a coach who knows them well.</p>
<ul>
<li><strong>Parents</strong> who want to get their fitness back after years of putting family first.</li>
<li><strong>Teenagers</strong> looking for martial arts, discipline and confidence.</li>
<li><strong>Weekend athletes</strong> who play football, run or cycle.</li>
</ul>"""),
            ("Martial arts for Kileleshwa families", """
<p>Jeet Kune Do and boxing fitness are popular with Kileleshwa families. For young people, martial arts training builds coordination, focus and respect, plus the confidence that comes from knowing how to handle yourself. Adults get a workout that is never boring. Learn more on our <a href="{root}services/jeet-kune-do-martial-arts.html">Jeet Kune Do training</a> page.</p>"""),
            ("Using Kileleshwa's quiet streets", """
<p>Compared with busier neighbourhoods, Kileleshwa's quieter roads suit early-morning walks and easy runs. We often programme light running or brisk walking on non-training days to build an aerobic base, while coached sessions focus on strength, technique and conditioning. Stay safe: run in daylight, face oncoming traffic and keep valuables at home.</p>"""),
            ("A balanced training week in Kileleshwa", """
<table>
<thead><tr><th>Day</th><th>Session</th></tr></thead>
<tbody>
<tr><td>Tuesday</td><td>Coached strength and conditioning</td></tr>
<tr><td>Thursday</td><td>Jeet Kune Do or boxing technique and pad rounds</td></tr>
<tr><td>Saturday</td><td>Coached full-body session or family martial arts</td></tr>
<tr><td>Other days</td><td>Easy walk or run, 10-minute mobility</td></tr>
</tbody>
</table>"""),
            ("Tips for staying fit in Kileleshwa", """
<ul class="ticks">
<li>Turn the school run into a walk where it is safe and practical.</li>
<li>Train at the same time each week so it becomes part of family routine.</li>
<li>Get the kids involved: bodyweight challenges are fun for all ages.</li>
<li>Prioritise sleep. It matters more than any supplement.</li>
</ul>"""),
        ],
        "faqs": [
            ("What age can children start martial arts?", "It depends on the child. Ask on WhatsApp and we will advise whether private or small-group sessions suit your child's age and experience."),
            ("Do you train weekend footballers in Kileleshwa?", "Yes. Strength and conditioning for footballers, including speed, power and injury prevention, is a core service."),
        ],
    },
    "lavington": {
        "sections": [
            ("Who we train in Lavington", """
<p>Lavington is one of Nairobi's established residential areas, with quiet roads off James Gichuru Road, Muthangari Drive and Gitanga Road. Clients here typically value professionalism, privacy and a clear plan. Many are executives, business owners and older adults who want to stay strong and mobile for decades.</p>
<ul>
<li><strong>Executives</strong> who want efficient sessions and measurable progress.</li>
<li><strong>Adults over 40</strong> focused on strength, mobility and healthy ageing.</li>
<li><strong>Clients returning from injury</strong> who need a careful, structured approach.</li>
</ul>"""),
            ("Strength and mobility for healthy ageing", """
<p>After 30, we gradually lose muscle unless we train to keep it. Strength training and mobility work are some of the most effective ways to stay independent, avoid falls and keep doing the things you love. For older Lavington clients, programmes focus on:</p>
<ol>
<li>Safe strength training for legs, back and grip.</li>
<li>Balance and single-leg stability.</li>
<li>Joint mobility for hips, shoulders and spine.</li>
<li>Low-impact conditioning that is easy on the joints.</li>
</ol>
<p>See our <a href="{root}services/mobility-flexibility.html">mobility and flexibility training</a> and <a href="{root}services/personal-training.html">one-on-one personal training</a> pages for more detail.</p>"""),
            ("Private, one-on-one coaching", """
<p>Some people simply do not enjoy busy gyms. One-on-one coaching means the whole session is about you: your technique, your pace, your goals. It also means sensitive topics like injuries, health conditions and confidence can be discussed openly and planned for properly.</p>"""),
            ("Tips for staying fit in Lavington", """
<ul class="ticks">
<li>Walk the quieter residential roads in the early morning for easy daily movement.</li>
<li>Schedule training like a business meeting, and protect the slot.</li>
<li>Track a few simple markers such as strength, waist measurement and sleep to see progress.</li>
<li>Combine strength training with daily mobility for the best long-term results.</li>
</ul>"""),
        ],
        "faqs": [
            ("Is strength training safe for people over 50?", "Yes, when properly coached and progressed. Strength training is one of the best things you can do for healthy ageing. Get medical clearance first if you have any health conditions."),
            ("Can you work alongside my physiotherapist?", "Yes. We are happy to follow your physiotherapist's guidance and build strength once you are cleared to train."),
        ],
    },
    "karen": {
        "sections": [
            ("Who we train in Karen", """
<p>Karen's space and greenery attract active people: runners on the roads around Karen Road and Langata Road, cyclists heading out towards Ngong, horse riders, golfers and families who spend their weekends outdoors. Clients here usually want to perform better at the activities they already love.</p>
<ul>
<li><strong>Runners and cyclists</strong> who need strength work to stay injury-free.</li>
<li><strong>Golfers</strong> who want better rotation and a stronger core.</li>
<li><strong>Families</strong> who want fun, active sessions together.</li>
</ul>"""),
            ("Strength training for endurance athletes", """
<p>Many runners and cyclists only run or ride. Adding two short strength sessions a week is one of the most effective ways to run faster, climb better and avoid common injuries like runner's knee and Achilles problems.</p>
<table>
<thead><tr><th>Exercise</th><th>Benefit for runners and cyclists</th></tr></thead>
<tbody>
<tr><td>Split squats and step-ups</td><td>Single-leg strength and knee stability</td></tr>
<tr><td>Romanian deadlifts</td><td>Hamstring and glute strength</td></tr>
<tr><td>Calf raises</td><td>Achilles and calf resilience</td></tr>
<tr><td>Planks and carries</td><td>Core stability for better posture late in a race</td></tr>
<tr><td>Hops and bounds</td><td>Elastic power and running economy</td></tr>
</tbody>
</table>
<p>Learn more on our <a href="{root}services/strength-conditioning.html">strength and conditioning</a> page.</p>"""),
            ("Outdoor training in Karen", """
<p>Karen's open spaces suit outdoor sessions: sprints, shadow boxing, pad work and bodyweight circuits in the fresh air. Training outdoors is also great for mental health. When the weather turns during the long rains, sessions move indoors so your progress does not stop.</p>"""),
            ("Tips for staying fit in Karen", """
<ul class="ticks">
<li>Use weekend trail walks near Ngong Road Forest as active recovery.</li>
<li>Add two strength sessions a week if you mainly run or cycle.</li>
<li>Hydrate well. Long outdoor sessions in the sun dehydrate you quickly.</li>
<li>Warm up properly before runs on cool mornings.</li>
</ul>"""),
        ],
        "faqs": [
            ("Can you help me train for a half marathon or marathon?", "Yes. We can add strength, mobility and conditioning work to support your running plan and reduce injury risk."),
            ("Do you train golfers?", "Yes. Mobility, rotational strength and core training can help golfers improve their swing and avoid back pain."),
        ],
    },
    "parklands": {
        "sections": [
            ("Who we train in Parklands", """
<p>Parklands is a lively, diverse neighbourhood stretching from Limuru Road across the numbered avenues towards Westlands. Clients include university students, young professionals, families and healthcare workers from the nearby hospitals. Many want effective, affordable training they can keep up for the long term.</p>
<ul>
<li><strong>Students</strong> who want to get fit and learn self-defence.</li>
<li><strong>Healthcare workers</strong> on shifts who need flexible scheduling.</li>
<li><strong>Families</strong> looking for active, confidence-building activities.</li>
</ul>"""),
            ("Affordable ways to train", """
<p>Personal training does not have to mean a big monthly bill. Popular options for Parklands clients include:</p>
<ol>
<li><strong>Small-group sessions:</strong> train with two or three friends and share the cost.</li>
<li><strong>Fewer sessions plus homework:</strong> one or two coached sessions a week, with a clear plan for the other days.</li>
<li><strong>Calisthenics-based programmes:</strong> no gym membership needed.</li>
</ol>
<p>Ask on WhatsApp for current rates and group options.</p>"""),
            ("Training for shift workers", """
<p>Nurses, doctors and other shift workers have some of the hardest schedules to train around. Programmes for shift workers focus on flexibility: shorter sessions, simple routines that can be done before or after a shift, and a strong emphasis on recovery and sleep. If a fixed weekly slot does not work, sessions can be booked week by week where availability allows.</p>"""),
            ("Calisthenics and boxing for students", """
<p>Bodyweight training and boxing fitness are perfect for students: minimal equipment, maximum results and skills that build confidence. Many students start by learning their first full push-up or pull-up and end up chasing advanced skills like the one-arm push-up. See our <a href="{root}services/calisthenics-training.html">calisthenics training</a> and <a href="{root}services/boxing-kickboxing-fitness.html">boxing fitness</a> pages.</p>"""),
            ("Tips for staying fit in Parklands", """
<ul class="ticks">
<li>Walk where it is safe and practical instead of taking short boda rides.</li>
<li>Find a training partner to keep each other accountable.</li>
<li>Try the 100 push-ups a day challenge, spread across the day.</li>
<li>Plan healthy, affordable meals around beans, eggs, vegetables and whole grains.</li>
</ul>"""),
        ],
        "faqs": [
            ("Do you offer student rates?", "Ask on WhatsApp about current rates and small-group options, which can make training more affordable."),
            ("Can shift workers book flexible sessions?", "Yes, where availability allows. Message us with your shift pattern and we will find workable times."),
        ],
    },
}
