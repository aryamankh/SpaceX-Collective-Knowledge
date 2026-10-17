import random, datetime
random.seed(20261110)
D = {
 'propulsion': ('prop','raptor-3','jakewmeyer',
   ['Raptor TVC actuator oscillation at 42 Hz','Turbopump chilldown cavitation on restart','Hot gas manifold leak after 30 s run','Igniter torch fouling on long coast','Regen channel pressure drop drift','Gimbal bearing fretting after static fire','Crossfeed transient during boostback','Chamber pressure sensor drift','LOX dome priming waterhammer','Engine controller reset under EMI','Thrust puck cracking on reflight','Mixture ratio trim during hover'],
   ['the TVC actuator','the turbopump','the igniter torch','the chamber pressure transducer','the gimbal bearing','the thrust puck']),
 'structures': ('str','starship-s38','mattythorne',
   ['Weld porosity in barrel gore seam','Ring frame buckling under axial load','Friction stir weld tool marks on tank wall','Tile rail pull-out after cryo cycle','Flap hinge lug fatigue','COPV overwrap delamination','Aft skirt bolt preload loss','Peel ply residue before primer','Cryo-shock crack at doubler edge','Ground handling dent criteria','Hoist lug proof load traceability','Section 3 out-of-roundness correction'],
   ['the gore seam','the ring frame','the tile rail','the hinge lug','the aft skirt fastener row','the doubler edge']),
 'avionics': ('av','flight-computer-b2','collierrgbsitisfise',
   ['Harness chafe at raceway exit','Flight computer watchdog reset','CAN bus termination fault','Connector keying mismatch on test rack','IMU thermal drift after pad soak','Power bus inrush trip','Telemetry frame drop on S-band','Redundant lane desync at boot','Lightning protection ground path','Battery cell imbalance on long pad','Actuator driver overcurrent false trip','Conformal coat masking error'],
   ['the harness bundle','the watchdog','the CAN termination','the IMU','the inrush limiter','the S-band transmitter']),
 'gnc': ('gnc','booster-b19','richiksc',
   ['Grid fin authority at high dynamic pressure','Attitude estimator divergence in coast','Flap scheduling overshoot on entry','Landing burn throttle quantization','Star tracker lost-in-space time','Control allocator saturation in transonic','Gyro bias calibration drift','Trajectory replan latency','Roll coupling in high wind','Sensor fusion weighting bug','Bank reversal chatter','Six-DOF sim fidelity versus flight'],
   ['the grid fin schedule','the attitude estimator','the flap scheduler','the throttle quantizer','the control allocator','the gyro bias estimate']),
 'thermal-protection': ('tps','starship-heat-shield','emmedve1',
   ['Tile gap filler erosion after reentry','Hex tile bonding voids','Aft flap seal char-through','Steel skin hot spot under missing tile','Tile density lot variation','RTV cure inhibition on cold pad','Blanket water ingress','Purge flow loss in tile cavity','Thermal soak through raceway penetration','Tile shear test sampling','Heat shield closeout inspection','Emissivity change from soot'],
   ['the gap filler','the tile bond line','the flap seal','the purge manifold','the closeout inspection','the shear sample']),
 'ground-systems': ('gse','ols-tower-2','kknox',
   ['Quick disconnect seal galling','Tanker detanking rate limit','Deluge valve slow close','Tower arm latch proximity sensor','GSE hose whip on disconnect','Cryo pump cavitation at high flow','Flame trench pressure transient','Methane detector false positive','Ship QD plate alignment','Booster transport saddle load','Hold-down preload drift','Ground purge dew point excursion'],
   ['the quick disconnect','the detank line','the deluge valve','the latch proximity sensor','the cryo pump','the hold-down clamp']),
 'manufacturing': ('mfg','high-bay-3','AstralZebulon',
   ['Gore panel fit-up tolerance stack','Friction stir weld parameter drift','Tooling datum shift after move','Laser tracker line-of-sight loss','Paint booth humidity control','Torque audit sampling rate','Rework traceability gap','Composite layup wrinkle','Springback compensation','Fastener hole positional tolerance','Cleanroom particle counts','Station takt time creep'],
   ['the fit-up fixture','the weld parameter set','the tooling datum','the laser tracker','the torque audit','the layup table']),
 'materials': ('mat','inconel-718','AlbericTrancart',
   ['Lot hardness spread on 718 plate','Plate inclusion inspection','COPV liner permeability','Seal swell in methalox','Primer adhesion on pickled steel','Fastener hydrogen embrittlement','Brazing flux residue corrosion','Ceramic tile density spec','Cryogenic seal leak rate scatter','Alloy cert traceability','Anodize thickness variation','Adhesive shelf life control'],
   ['the incoming plate lot','the liner wall','the face seal','the primer layer','the fastener lot','the adhesive batch']),
 'flight-software': ('sw','flight-software-v7','aryamankha',
   ['Watchdog timeout during engine start','Mode transition race in sequencer','Parameter table version skew','Telemetry encoder buffer overrun','Fault masking on second fault','Boot image rollback failure','Control loop timing jitter','Abort rule false positive','Config hash mismatch at load','Logging backpressure','Sim-in-the-loop coverage gap','Patch rollback after hotfire'],
   ['the watchdog timer','the mode sequencer','the parameter table','the telemetry encoder','the fault tree','the abort rule']),
 'flight-ops': ('ops','launch-complex-39a','CAM-Gerlach',
   ['Range call timing on hold','Weather scrub decision tree','Pad crew handover checklist','Chase plane comms loss','Recovery fleet positioning','Tanking sequence conflict','Crew rest versus window trade','Countdown poll drift','Range asset conflict resolution','Post-flight downlink priority','Anomaly triage during ascent','Observer exclusion zones'],
   ['the range call','the weather rule set','the handover checklist','the tanking sequence','the countdown poll','the triage rota']),
 'safety': ('saf','pad-operations','shahar603',
   ['Mishap closeout review cadence','Hazard analysis stale after mod','Lockout tagout on GSE','LOX spill response drill','Confined space entry on tank','Fall protection at height 40 m','Pressure test exclusion zone','Forklift pedestrian separation','Cryo burn first aid placement','Near-miss reporting rate drop','PPE compliance audit','Emergency egress lighting check'],
   ['the closeout review','the hazard analysis','the lockout tagout kit','the spill drill','the exclusion zone','the egress lighting']),
}
REV = ['CAM-Gerlach','kknox','mattythorne','shahar603','jhpratt']
PHASE = ['a static fire','a cryo proof','the first integrated flight','a reflight turnaround','a night tanking','a wet dress rehearsal']
SIGNAL = ['pressure','vibration','temperature','current draw','strain','leak rate','frame timing','valve position']
ACTION = ['held at T-4 s','cut short','aborted by the operator','run to completion with a note','paused for inspection']
DOC = ['the run log','the NCR','the teardown report','the telemetry slice','the inspection photo set','the torque audit sheet']
CHECK = ['a pre-run visual','a torque re-verification','a leak check','an endoscope pass','a dimensional check','a functional test']
SPEC = ['the torque spec','the purge dwell','the chilldown ramp','the inspection interval','the acceptance band','the sampling rate']
today = datetime.date(2026, 10, 29)
n = 0
for dom, (ab, system, author, titles, things) in D.items():
    for title in titles:
        d = today - datetime.timedelta(days=random.randint(20, 900))
        slug = '-'.join(title.lower().replace(',', '').replace('.', '').split())[:48]
        nid = f'{ab}-{slug}-{d.year}-{d.month:02d}'
        thing = random.choice(things)
        sev = random.choice(['low','medium','high','high','critical'])
        body = f"""## Context

{random.choice(PHASE).capitalize()} on {system}, while {thing} was under watch by the console. The run was configured to the current published limits.

## What happened

{random.choice(SIGNAL).capitalize()} on {thing} moved outside the expected band within {random.randint(2,40)} s. The run was {random.choice(ACTION)}. No hardware was lost beyond the item already suspect.

## Root cause

{thing.capitalize()} had accumulated wear that the periodic inspection did not resolve at the resolution needed. Teardown found the condition; the {random.choice(DOC)} records it with photos.

## What we changed

{random.choice(SPEC).capitalize()} was revised and {random.choice(CHECK)} was added to the task list before the next run. Owner: {author}.

## What we would do differently

Stop on the first excursion of {thing} instead of waiting for a second confirmation. Two data points cost more than the abort.

## Evidence

{random.choice(DOC).capitalize()}, telemetry export and teardown photos filed against this note. Related notes are linked from the domain index.
"""
        fm = f"""---
id: {nid}
domain: {dom}
system: {system}
author: {author}
reviewed_by: {random.choice([r for r in REV if r != author])}
status: reviewed
severity: {sev}
created: {d.isoformat()}
tags: [{', '.join(sorted(set([dom.split('-')[0], thing.split()[-1], random.choice(['reflight','hotfire','cryo','pad','turnaround'])])))}]
---

# {title}

"""
        open(f'knowledge/{dom}/{nid}.md', 'w', encoding='utf-8', newline='\n').write(fm + body)
        n += 1
print('notes', n)
