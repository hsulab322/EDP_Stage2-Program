#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 (v2021.2.0) by Yen-Ting Li,
    on 七月 04, 2021, at 08:26
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""
from __future__ import absolute_import, division
from PIL.Image import FASTOCTREE
from psychopy import gui, visual ,core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import math
import random
import os  # handy system and path functions
import sys
import pandas as pd

from psychopy.hardware import keyboard
from pyglet.window.mouse import buttons_string

from driveapi import driveapi

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.0'
expName = 'EDP_stage2'  # from the Builder filename that created this script
expInfo = {'participant': '',
            'alpha': 1.0,
            'beta': 1.0,
            'max_gain':'10000',
            'max_loss':'10000',
            'experiment': ['Behavior','MRS-fMRI','PET-fMRI']}

dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr(format = "%Y-%m-%d-%H%M")  # add a simple timestamp #Year-Month-Day-HourMin
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc

filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
dfname = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], 'DataFrame', expInfo['date'])
print(filename)


####################
# # determine if application is a script file or frozen exe
# if getattr(sys, 'frozen', False):
#     application_path = os.path.dirname(sys.executable)
# else:
#     application_path = _thisDir

# filename = application_path + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
# dfname = application_path + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], 'DataFrame', expInfo['date'])
# # print(filename)
#####################


# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file


endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Setup the Window
win = visual.Window(
    size=[1280,720], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='test', color= [0.25,0.25,0.25] , colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')

# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Round"
interface_Round_List=[
'./interface/Round 1.png','./interface/Round 2.png','./interface/Round 3.png','./interface/Round 4.png',
'./interface/Round 5.png','./interface/Round 6.png','./interface/Round 7.png','./interface/Round 8.png',
'./interface/Round 9.png','./interface/Round 10.png','./interface/Round 11.png','./interface/Round 12.png']

RoundClock = core.Clock()
interface_Round = visual.ImageStim(
    win=win,
    name='interface_Round', 
    image=None, mask=None,
    ori=0.0, pos=(0, 0), size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
mouse_Round = event.Mouse(win=win)
x, y = [None, None]
mouse_Round.mouseClock = core.Clock()
key_Round = keyboard.Keyboard()
OK_Round = visual.ImageStim(
    win=win,
    name='OK_Round', 
    image='./interface/buttonOK.png', mask=None,
    ori=0.0, pos=(0, -300), size=(225,114),#150,76
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "Interval"
IntervalClock = core.Clock()
cross = visual.ShapeStim(
    win=win, name='cross', vertices='cross',
    size=(45,45),#30,30
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,  lineColor='black', fillColor='black',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "Lottery"
LotteryClock = core.Clock()
interface_Lottery = visual.ImageStim(
    win=win,
    name='interface_lottery', 
    image='./interface/lottery.png', mask=None,
    ori=0.0, pos=(0, 0), size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text_up_Lottery = visual.TextStim(win=win, name='text_up_Lottery',
    text='None',
    font='Calibri',
    pos=(280,280), height=75, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0)
text_down_Lottery = visual.TextStim(win=win, name='text_down_Lottery',
    text='None',
    font='Calibri',
    pos=(280,-35), height=75, wrapWidth=None, ori=0, 
    color=(217,0,0), colorSpace='rgb255', opacity=1, 
    languageStyle='LTR',
    depth=-5.0)

# Initialize components for Routine "Choice"
ChoiceClock = core.Clock()
mouse_Choice = event.Mouse(win=win)
x, y = [None, None]
mouse_Choice.mouseClock = core.Clock()
key_Choice = keyboard.Keyboard()
Quit = visual.ImageStim(
    win=win,
    name='Quit', 
    image='./interface/Quit.png', mask=None,
    ori=0.0, pos=(-300,-0), size=(288, 162), #128,72
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Bet = visual.ImageStim(
    win=win,
    name='Bet', 
    image='./interface/Bet.png', mask=None,
    ori=0.0, pos=(300,0), size=(288, 162), #128,72
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
OK_Choice = visual.ImageStim(
    win=win,
    name='OK_Choice', 
    image=None, mask=None,
    ori=0, pos=(0, -250), size=(270,140), #120,62
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "Outcome"
OutcomeClock = core.Clock()
interface_Outcome = visual.ImageStim(
    win=win,
    name='interface_Outcome', 
    image=None, mask=None,
    ori=0.0, pos=(0, 0), size=(1920,1080),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text_outcome = visual.TextStim(win=win, name='text_outcome',
    text=9999,
    font='Calibri',
    pos=(0, 0), height=100, wrapWidth=1000, ori=0, 
    color=(-1,-1,-1), colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0)

# Initialize components for Routine "Incentive"
incentiveClock = core.Clock()
interface_incentive = visual.ImageStim(
    win=win,
    name='interface_incentive', 
    image='./interface/incentive_1.png', mask=None,
    ori=0.0, pos=(0, 0), size=[1920,1080],
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
OK_incentive = visual.ImageStim(
    win=win,
    name='OK_incentive', 
    image='./interface/buttonOK.png', mask=None,
    ori=0.0, pos=(0, -450), size=(150,76), #150,76
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
mouse_incentive = event.Mouse(win=win)
x, y = [None, None]
mouse_incentive.mouseClock = core.Clock()
key_incentive = keyboard.Keyboard()
text_summary = visual.TextStim(win=win, name='text_summary',
    text='Game Summary',
    font='Calibri',
    pos=(0, 450), height=80, wrapWidth=1000, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0)


# Initialize components for Routine "endExp"
endExpClock = core.Clock()
text_endExp = visual.TextStim(win=win, name='endExp',
    text='實驗結束',
    font='Calibri',
    pos=(0, 200), height=60, wrapWidth=1280, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-0.0);
text_final_reward = visual.TextStim(win=win, name='endExp',
    text='',
    font='Calibri',
    pos=(0, 0), height=60, wrapWidth=1280, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-0.0);
OK_endExp = visual.ImageStim(
    win=win,
    name='OK_endExp', 
    image='./interface/buttonOK.png', mask=None,
    ori=0.0, pos=(0, -300), size=(225,114), #150,76
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
mouse_endExp = event.Mouse(win=win)
x, y = [None, None]
mouse_endExp.mouseClock = core.Clock()
key_endExp = keyboard.Keyboard()

# Create some handy timers
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 


# create a DataFrame
stage2df = pd.DataFrame(columns = ['Round','Trial','Gain','Loss','Choice','Outcome','Delta','Onset','Offset'])


# PTU 參數
subject = expInfo['participant']
alpha = expInfo['alpha']
beta = expInfo['beta']
max_gain = int(expInfo['max_gain'])
max_loss = int(expInfo['max_loss'])

# 紀錄受試者參數資料到.csv
thisExp.addData('Subject', expInfo['participant'])
thisExp.addData('alpha', alpha)
thisExp.addData('beta', beta)
thisExp.addData('max_gain',max_gain)
thisExp.addData('max_loss',max_loss)

# ratio_List
ratio_List = [0.1, 0.3, 0.5, 0.7, 0.9, 1.0, 1.1, 1.3, 1.5]
lenTrial = len(ratio_List)

# PTU 函數
def PTU (Trial_n, x):
    ratio = ratio_List[Trial_n]
    Ug = (x/max_gain)**alpha
    Ul = Ug * ratio
    xstar = round(-1 * max_loss * Ul**(1/beta))
    return xstar

# 建立資料dictionary    
base_value = 200
delta_dict = {**{'delta_'+str(i):[(i+1)%8*base_value] for i in range(1,7)},**{'delta_'+str(i+6):[(i+1)%8*base_value] for i in range(1,7)}}

x_dict = {**{'x_List_'+str(i):[(i+1)%8*base_value//2] for i in range(1,7)},**{'x_List_'+str(i+6):[(i+1)%8*base_value//2] for i in range(1,7)}}
x_star_dict = {**{'x_star_List_'+str(i):[PTU(0,x_dict['x_List_'+str(i)][-1])] for i in range(1,7)},**{'x_star_List_'+str(i+6):[PTU(0,x_dict['x_List_'+str(i+6)][-1])] for i in range(1,7)}}
incentive_list = [] # data list used in the incentive phase

# x_dict = {'x_List_'+str(i):None for i in range(1,13)}
# x_star_dict = {'x_star_List_'+str(i):None for i in range(1,13)}
# delta_dict = {'delta_'+str(i):[0] for i in range(1,13)}


# 建立Round順序
Round_order_List = ['Round_'+str(i+1) for i in range(12)]

random_trial_order = [0,1,2,3,4,5]
seq2 = [6,7,8,9,10,11]
random.shuffle(random_trial_order)
random.shuffle(seq2)
while random_trial_order[-1]+6 == seq2[0]:
    random.shuffle(seq2)
random_trial_order.extend(seq2)
print(random_trial_order)

# Round: 顯示第幾個round
# Random isi: 1s, 3s
# Lottery: show lottery: 8s
# random Interval before choice :1s,2s,3s
# Choice: Quit or Bet: max: 10s
# Outcome: 贏或輸: 3s

globalClock = core.Clock()
# text_waitfMRI = visual.TextStim(win=win, name='waitFMRI',text='Waiting for the trigger \n press esc to quit',color='black',height=80, wrapWidth = 10000 ,pos = (0,100))
# text_expinfo = visual.TextStim(win=win, name='expinfo',  color='black',pos = (0,-300), height = 30, text = f'Participant: {subject} \n Alpha: {alpha} \n Beta: {beta} \n Max_gain: {max_gain} \n Max_lost: {max_loss}')
# text_waitfMRI.tStartRefresh = None
# text_waitfMRI.tStopRefresh = None
# text_waitfMRI.draw()
# text_expinfo.draw()
# win.timeOnFlip(text_waitfMRI, 'tStartRefresh')
# win.flip()
# a = event.waitKeys(keyList=['5','escape'])
# text_waitfMRI.tStopRefresh = core.getTime()
# if a[-1] == 'escape':
#     core.quit()
# win.flip()

# thisExp.addData('text_waitfMRI.started', text_waitfMRI.tStartRefresh)
# thisExp.addData('text_waitfMRI.stopped', text_waitfMRI.tStopRefresh)

# initialization ends
present_interface_round = 0
for r in random_trial_order: # random_trial_order: # 12個Round
    #要顯示的round名稱
    interface_Round.image = interface_Round_List[present_interface_round]
    present_interface_round += 1

    # ------Prepare to start Routine "Round"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_Round
    mouse_Round.clicked_name = []
    _key_Round_allKeys = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    RoundComponents = [interface_Round, mouse_Round, OK_Round, key_Round]
    for thisComponent in RoundComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    RoundClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "Round"-------
    while continueRoutine:
        # get current time
        t = RoundClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=RoundClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)

        # update/draw components on each frame
        
        # *interface_Round* updates
        if interface_Round.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            interface_Round.frameNStart = frameN  # exact frame index
            interface_Round.tStart = t  # local t and not account for scr refresh
            interface_Round.tStartRefresh = tThisFlipGlobal  # on global time
            # assign lastflip time to tStartRefresh until next flip
            win.timeOnFlip(interface_Round, 'tStartRefresh')  # time at next scr refresh 
            interface_Round.setAutoDraw(True)
        # *mouse_Round* updates
        if mouse_Round.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_Round.frameNStart = frameN  # exact frame index
            mouse_Round.tStart = t  # local t and not account for scr refresh
            mouse_Round.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_Round, 'tStartRefresh')  # time at next scr refresh
            mouse_Round.status = STARTED
            mouse_Round.mouseClock.reset()
            prevButtonState = mouse_Round.getPressed()  # if button is down already this ISN'T a new click
        if mouse_Round.status == STARTED:  # only update if started and not finished!
            buttons = mouse_Round.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(OK_Round)
                        clickableList = OK_Round
                    except:
                        clickableList = [OK_Round]
                    for obj in clickableList:
                        if obj.contains(mouse_Round):
                            gotValidClick = True
                            mouse_Round.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
            # *key_Round* updates
            waitOnFlip = False
            if key_Round.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_Round.frameNStart = frameN  # exact frame index
                key_Round.tStart = t  # local t and not account for scr refresh
                key_Round.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_Round, 'tStartRefresh')  # time at next scr refresh
                key_Round.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_Round.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_Round.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_Round.status == STARTED and not waitOnFlip:
                theseKeys = key_Round.getKeys(keyList=['6'], waitRelease=True)
                _key_Round_allKeys.extend(theseKeys)
                if len(_key_Round_allKeys):
                    # a response ends the routine
                    continueRoutine = False

        # *OK_Round* updates
        if OK_Round.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            OK_Round.frameNStart = frameN  # exact frame index
            OK_Round.tStart = t  # local t and not account for scr refresh
            OK_Round.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(OK_Round, 'tStartRefresh')  # time at next scr refresh
            OK_Round.setAutoDraw(True)
        

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RoundComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "Round"-------
    for thisComponent in RoundComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
            thisComponent.tStopRefresh = tThisFlipGlobal
            thisComponent.tStop = tThisFlip
    thisExp.addData('interface_Round.started' + '_' + str(r+1), interface_Round.tStartRefresh)
    thisExp.addData('interface_Round.stopped' + '_' + str(r+1), interface_Round.tStopRefresh)
    stage2df = stage2df.append({'Round':str(r+1),
                                'Trial':f'Round_{r+1}_start',
                                'Onset':interface_Round.tStartRefresh,
                                'Offset':interface_Round.tStopRefresh},
                                ignore_index=True)
    routineTimer.reset()

    # Round Phase ends


# ------Prepare to start the Trial-------

    # create a list for every round to save the choice and outcome for every trial in each round
    Choice_List = [] # Choice List for round `r`
    Outcome_List = [] # Outcome List for round `r`

    # 每個list是屬於該Round，pass by reference
    x_nowDictList = x_dict['x_List_'+str(r+1)]
    x_star_nowDictList = x_star_dict['x_star_List_'+str(r+1)]
    delta_nowDictList = delta_dict['delta_'+str(r+1)]


    for Trial_n in range(0, lenTrial): # 每個Round總共7個trial 0,1,2,3,4,5,6
    # ------Prepare to start Routine "Interval"-------
        continueRoutine = True
        isi = random.choice([1,3])
        routineTimer.add(isi) # 間隔時間 isi
        # update component parameters for each repeat
        # keep track of which components have finished
        IntervalComponents = [cross]
        for thisComponent in IntervalComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        IntervalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

    # -------Run Routine "Interval"-------
        print(r+1,'-',Trial_n+1,sep="") # show current Round-Trial
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = IntervalClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=IntervalClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cross* updates
            if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cross.frameNStart = frameN  # exact frame index
                cross.tStart = t  # local t and not account for scr refresh
                cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
                cross.setAutoDraw(True)
            if cross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cross.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    cross.tStop = t  # not accounting for scr refresh
                    cross.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(cross, 'tStopRefresh')  # time at next scr refresh
                    cross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in IntervalComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

    # -------Ending Routine "Interval"-------
        for thisComponent in IntervalComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
                thisComponent.tStopRefresh = tThisFlipGlobal
        # Save the data
        thisExp.addData('interval.started' + '_' + str(r+1) + "-" + str(Trial_n+1), cross.tStartRefresh)
        thisExp.addData('interval.stopped' + '_' + str(r+1) + "-" + str(Trial_n+1), cross.tStopRefresh)
        stage2df = stage2df.append({'Round': str(r+1),
                                    'Trial': 'interval_'+str(Trial_n+1),
                                    'Onset': cross.tStartRefresh,
                                    'Offset': cross.tStopRefresh}
                                    ,ignore_index=True)
        


    # ------Prepare to start Routine "Lottery"-------
        # Lottery Phase start # `r` is the index of Round , starts from 0 to 11

        # Gain and Loss outcome show in the current trial `Trial_n`

        if Trial_n != 0 :
            x_nowDictList.append(round(delta_nowDictList[-1]/2 + x_nowDictList[-1]))
            x_star_nowDictList.append(PTU(Trial_n,x_nowDictList[-1]))

        print('gain list',x_nowDictList)
        print('loss list',x_star_nowDictList)
        print('c',delta_nowDictList)

        Positive_Outcome = x_nowDictList[Trial_n] 
        Negative_Outcome = x_star_nowDictList[Trial_n]
        # Show current gain and loss
        print("Gain: ",Positive_Outcome)
        print("Loss: ",Negative_Outcome)

        # assigning values to text object
        text_up_Lottery.text = Positive_Outcome
        text_down_Lottery.text = Negative_Outcome

        # assign pic path to button object (to re-assign every trial)
        Quit.image='./interface/Quit.png'
        Bet.image='./interface/Bet.png'
        OK_Choice.image=None # Do not show OK at the beginning of the trial

        win.mouseVisible=True
        continueRoutine = True
        # update component parameters for each repeat
        # setup some python lists for storing info about the mouse_Choice
        mouse_Choice.clicked_name = []
        gotValidClick = False  # until a click is received
        key_Choice.keys = []
        key_Choice.rt = []
        _key_Choice_allKeys = []
        # keep track of which components have finished
        LotteryComponents = [interface_Lottery, text_up_Lottery, text_down_Lottery]
        for thisComponent in LotteryComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        LotteryClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

    # -------Run Routine "Lottery"-------
        validChoice = False
        ifRelease = False
        routineTimer.add(8) # Lottery time 8s
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = LotteryClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=LotteryClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *interface_Lottery* updates
            if interface_Lottery.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                interface_Lottery.frameNStart = frameN  # exact frame index
                interface_Lottery.tStart = t  # local t and not account for scr refresh
                interface_Lottery.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(interface_Lottery, 'tStartRefresh')  # time at next scr refresh
                interface_Lottery.setAutoDraw(True)

            # *text_up_Lottery* updates
            if text_up_Lottery.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_up_Lottery.frameNStart = frameN  # exact frame index
                text_up_Lottery.tStart = t  # local t and not account for scr refresh
                text_up_Lottery.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_up_Lottery, 'tStartRefresh')  # time at next scr refresh
                text_up_Lottery.setAutoDraw(True)
            
            # *text_down_Lottery* updates
            if text_down_Lottery.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_down_Lottery.frameNStart = frameN  # exact frame index
                text_down_Lottery.tStart = t  # local t and not account for scr refresh
                text_down_Lottery.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_down_Lottery, 'tStartRefresh')  # time at next scr refresh
                text_down_Lottery.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in LotteryComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

    # -------Ending Routine "Lottery"-------

        for thisComponent in LotteryComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
                thisComponent.tStopRefresh = tThisFlipGlobal
        thisExp.addData('interface_Lottery.started' + '_' + str(r+1) + '-' + str(Trial_n+1) , interface_Lottery.tStartRefresh)
        thisExp.addData('interface_Lottery.stopped' + '_' + str(r+1) + '-' + str(Trial_n+1) , interface_Lottery.tStopRefresh)
        stage2df = stage2df.append({'Round': str(r+1),
                                    'Trial': 'Lottery_'+str(Trial_n+1),
                                    'Gain':x_nowDictList[Trial_n],
                                    'Loss':x_star_nowDictList[Trial_n],
                                    'Onset': interface_Lottery.tStartRefresh,
                                    'Offset': interface_Lottery.tStopRefresh}
                                    ,ignore_index=True)

        # the Routine "Lottery" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()

    # ------Prepare to start Routine "random Interval"-------
        continueRoutine = True
        iri = random.randint(1,3) # 1,2,3
        routineTimer.add(iri) # 隨機間隔時間
        # update component parameters for each repeat
        # keep track of which components have finished
        IntervalComponents = [cross]
        for thisComponent in IntervalComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        IntervalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

    # -------Run Routine "random Interval"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = IntervalClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=IntervalClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cross* updates
            if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cross.frameNStart = frameN  # exact frame index
                cross.tStart = t  # local t and not account for scr refresh
                cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
                cross.setAutoDraw(True)
            if cross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cross.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    cross.tStop = t  # not accounting for scr refresh
                    cross.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(cross, 'tStopRefresh')  # time at next scr refresh
                    cross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in IntervalComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

    # -------Ending Routine "random Interval"-------
        for thisComponent in IntervalComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
                thisComponent.tStopRefresh = tThisFlipGlobal
        
        # save the data
        thisExp.addData('random_Interval.started' + '_' + str(r+1) + "-" + str(Trial_n+1), cross.tStartRefresh)
        thisExp.addData('random_Interval.stopped' + '_' + str(r+1) + "-" + str(Trial_n+1), cross.tStopRefresh)
        stage2df = stage2df.append({'Round': str(r+1),
                                    'Trial': 'Random_Interval_'+str(Trial_n+1),
                                    'Onset': cross.tStartRefresh,
                                    'Offset': cross.tStopRefresh}
                                    ,ignore_index=True)
        routineTimer.reset()

    # ------Prepare to start Routine "Choice"-------
        win.mouseVisible=True
        continueRoutine = True
        routineTimer.add(10) #  choicetime = 10
        # update component parameters for each repeat
        # setup some python lists for storing info about the mouse_Choice
        mouse_Choice.clicked_name = []
        gotValidClick = False  # until a click is received
        key_Choice.keys = []
        key_Choice.rt = []
        _key_Choice_allKeys = []
        # keep track of which components have finished
        ChoiceComponents = [mouse_Choice, Quit, Bet, OK_Choice, key_Choice]
        for thisComponent in ChoiceComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ChoiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
    # -------Run Routine "Choice"-------
        validChoice = False
        ifRelease = False
        endTrial = False
        currentChoice = "Quit"
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ChoiceClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ChoiceClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *mouse_Choice* updates
            if mouse_Choice.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_Choice.frameNStart = frameN  # exact frame index
                mouse_Choice.tStart = t  # local t and not account for scr refresh
                mouse_Choice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_Choice, 'tStartRefresh')  # time at next scr refresh
                mouse_Choice.status = STARTED
                mouse_Choice.mouseClock.reset()
                prevButtonState = mouse_Choice.getPressed()  # if button is down already this ISN'T a new click
            if mouse_Choice.status == STARTED:  # only update if started and not finished!
                buttons = mouse_Choice.getPressed()
                if buttons != prevButtonState and validChoice:
                    ifRelease = True
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [Quit,Bet]:
                        if obj.contains(mouse_Choice):
                            gotValidClick = True
                            mouse_Choice.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        prevButtonState = buttons[:]
                        ifRelease = False
                        if mouse_Choice.isPressedIn(Quit): 
                            currentChoice = "Quit"
                            Bet.image='./interface/Bet.png'
                            Quit.image='./interface/Quit_selected.png'
                            OK_Choice.image='./interface/buttonOK.png'
                            validChoice = True
                        elif mouse_Choice.isPressedIn(Bet):
                            currentChoice = "Bet"
                            Bet.image='./interface/Bet_selected.png'
                            Quit.image='./interface/Quit.png'
                            OK_Choice.image='./interface/buttonOK.png'
                            validChoice = True
                if sum(buttons) > 0 and validChoice: # and ifRelease:  # state has changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    for obj in [OK_Choice]:
                        if obj.contains(mouse_Choice):
                            endTrial = True
                            continueRoutine = False
                            

            # *key_Choice* updates
            waitOnFlip = False
            if key_Choice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_Choice.frameNStart = frameN  # exact frame index
                key_Choice.tStart = t  # local t and not account for scr refresh
                key_Choice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_Choice, 'tStartRefresh')  # time at next scr refresh
                key_Choice.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_Choice.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_Choice.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_Choice.status == STARTED and not waitOnFlip:
                gotValidKey = False
                theseKeys = key_Choice.getKeys(keyList=['3','4'], waitRelease=True)
                _key_Choice_allKeys.extend(theseKeys)
                if len(_key_Choice_allKeys):
                    gotValidKey = True
                    key_Choice.keys = _key_Choice_allKeys[-1].name  # just the last key pressed
                    key_Choice.rt = _key_Choice_allKeys[-1].rt
                if key_Choice.keys == '3':
                    currentChoice = "Quit"
                    Bet.image='./interface/Bet.png'
                    Quit.image='./interface/Quit_selected.png'
                    OK_Choice.image='./interface/buttonOK.png'
                    validChoice = True
                elif key_Choice.keys == '4':
                    currentChoice = "Bet"
                    Bet.image='./interface/Bet_selected.png'
                    Quit.image='./interface/Quit.png'
                    OK_Choice.image='./interface/buttonOK.png'
                    validChoice = True

            # a response ends the routine
            endKey = key_Choice.getKeys(keyList=['6'], waitRelease=True)
            if len(endKey) and validChoice:
                endTrial = True
                continueRoutine = False


            # *OK_Choice* updates
            if OK_Choice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                OK_Choice.frameNStart = frameN  # exact frame index
                OK_Choice.tStart = t  # local t and not account for scr refresh
                OK_Choice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(OK_Choice, 'tStartRefresh')  # time at next scr refresh
                OK_Choice.setAutoDraw(True)
            
            # *Quit* updates
            if Quit.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Quit.frameNStart = frameN  # exact frame index
                Quit.tStart = t  # local t and not account for scr refresh
                Quit.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Quit, 'tStartRefresh')  # time at next scr refresh
                Quit.setAutoDraw(True)
            
            # *Bet* updates
            if Bet.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Bet.frameNStart = frameN  # exact frame index
                Bet.tStart = t  # local t and not account for scr refresh
                Bet.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Bet, 'tStartRefresh')  # time at next scr refresh
                Bet.setAutoDraw(True)

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                print(currentChoice)
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ChoiceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
    # -------Ending Routine "Choice"-------
        for thisComponent in ChoiceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
                thisComponent.tStopRefresh = tThisFlipGlobal

        # store data for thisExp

        thisExp.addData('interface_Choice.started' + '_' + str(r+1) + '-' + str(Trial_n+1) , Quit.tStartRefresh)
        thisExp.addData('interface_Choice.stopped' + '_' + str(r+1) + '-' + str(Trial_n+1) , Quit.tStopRefresh)

        if currentChoice == 'Quit' or not endTrial :
            Choice_List.append('Quit')
            if Trial_n == 0:
                incentive_list.append(['Round '+str(r+1), 'Quit'])
                print(incentive_list[-1])
            elif Outcome_List[-1] == 'Win':
                incentive_list.append(['Round '+str(r+1), x_nowDictList[Trial_n-1]])
                print(incentive_list[-1])
            else:
                incentive_list.append(['Round '+str(r+1), x_star_nowDictList[Trial_n-1]])
                print(incentive_list[-1])

            stage2df = stage2df.append({'Round':str(r+1),
                                        'Trial':'Choice_'+str(Trial_n+1),
                                        'Gain':x_nowDictList[Trial_n],
                                        'Loss':x_star_nowDictList[Trial_n],
                                        'Choice':'Quit',
                                        'Delta':delta_nowDictList[Trial_n],
                                        'Onset':Quit.tStartRefresh,
                                        'Offset':Quit.tStopRefresh}
                                        ,ignore_index=True)

        elif currentChoice == 'Bet':
            Choice_List.append('Bet')
            WinorLose = random.randint(0,1) # 0 = lose, 1 = win
            if WinorLose == 0:
                Outcome_List.append('Lose')
                print("Lose")
                print()
                if Trial_n == 0:
                    nextChips = delta_nowDictList[Trial_n] + Negative_Outcome
                    delta_nowDictList.append(nextChips)
                elif Trial_n != lenTrial-1:
                    nextChips = 0.5 * delta_nowDictList[Trial_n] + Negative_Outcome
                    delta_nowDictList.append(nextChips)
                elif Trial_n == lenTrial-1: # last trial
                    incentive_list.append(['Round '+str(r+1), x_star_nowDictList[Trial_n]])
                    print(incentive_list[-1])

            else:
                Outcome_List.append('Win')
                print("Win")
                print()
                if Trial_n == 0:
                    nextChips = delta_nowDictList[Trial_n] + Positive_Outcome
                    delta_nowDictList.append(nextChips)
                elif Trial_n != lenTrial-1:
                    nextChips = 0.5 * delta_nowDictList[Trial_n] + Positive_Outcome
                    delta_nowDictList.append(nextChips)
                elif Trial_n == lenTrial-1:  # last trial
                    incentive_list.append(['Round '+str(r+1),x_nowDictList[Trial_n]])
                    print(incentive_list[-1])

            if nextChips < 0: 
                print("run out of chips")
                print()
                incentive_list.append(['Round '+str(r+1), x_star_nowDictList[Trial_n]])
                print(incentive_list[-1])                

            stage2df = stage2df.append({'Round':str(r+1),
                                        'Trial':'Choice_'+str(Trial_n+1),
                                        'Gain':x_nowDictList[Trial_n],
                                        'Loss':x_star_nowDictList[Trial_n],
                                        'Choice':'Bet',
                                        'Outcome':Outcome_List[-1],
                                        'Delta':delta_nowDictList[Trial_n],
                                        'Onset':Quit.tStartRefresh,
                                        'Offset':Quit.tStopRefresh}
                                        ,ignore_index=True)




        thisExp.addData('Choice_'+ Round_order_List[r], Choice_List)
        thisExp.addData('Outcome_'+ Round_order_List[r], Outcome_List)
        thisExp.addData('x_'+ Round_order_List[r], x_nowDictList)
        thisExp.addData('x_star_'+ Round_order_List[r], x_star_nowDictList)
        thisExp.addData('delta_'+ Round_order_List[r],delta_nowDictList)

        # print("x_now",x_nowDictList)
        # print("x_star_now",x_star_nowDictList)
        # print("delta_now",delta_nowDictList)
        # print(stage2df)
        # print(incentive_dict)


        # the Routine "Lottery" was not non-slip safe, so reset the non-slip timer
        if Choice_List[-1] == 'Quit':
            routineTimer.reset()
            break
        routineTimer.reset()
        

    # ------Prepare to start Routine "Outcome"-------
        if Outcome_List[-1] == 'Win':
            text_outcome.color = (-1,-1,1)
            text_outcome.text = f"You won {x_nowDictList[Trial_n]} chips"
        elif Outcome_List[-1] == 'Lose':
            text_outcome.color = (0.7020,-1,-1)
            if delta_nowDictList[-1] > 0:
                text_outcome.text = f"You lost {-x_star_nowDictList[Trial_n]} chips"
            else:
                text_outcome.text = f"You lost {-x_star_nowDictList[Trial_n]} chips\n\nYou've run out of chips"
            


        continueRoutine = True
        routineTimer.add(3) #3s
        # update component parameters for each repeat
        # keep track of which components have finished
        IntervalComponents = [text_outcome]
        for thisComponent in IntervalComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        IntervalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

    # -------Run Routine "Outcome"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = IntervalClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=IntervalClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *text_outcome* updates
            if text_outcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_outcome.frameNStart = frameN  # exact frame index
                text_outcome.tStart = t  # local t and not account for scr refresh
                text_outcome.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_outcome, 'tStartRefresh')  # time at next scr refresh
                text_outcome.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in IntervalComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

    # -------Ending Routine "Outcome"-------
        for thisComponent in IntervalComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
                thisComponent.tStopRefresh = tThisFlipGlobal
        thisExp.addData('text_outcome.started' + '_' + str(r+1) + "-" + str(Trial_n+1), text_outcome.tStartRefresh)
        thisExp.addData('text_outcome.stopped' + '_' + str(r+1) + "-" + str(Trial_n+1), text_outcome.tStopRefresh)
        stage2df = stage2df.append({'Round': str(r+1),
                                    'Trial': 'Outcome_'+str(Trial_n+1),
                                    'Outcome':Outcome_List[-1],
                                    'Delta':delta_nowDictList[-1],
                                    'Onset': text_outcome.tStartRefresh,
                                    'Offset': text_outcome.tStopRefresh}
                                    ,ignore_index=True)

        # save to csv every trial
        stage2df.to_csv(dfname+'.csv',index=False)
        routineTimer.reset()
        if delta_nowDictList[-1] <= 0:
            break







"""
0 4 8
1 5 9
2 6 10
3 7 11
"""
#left and upmost lottery
xpos = 0
ypos = 0
text_incentive_list=[]
count = 0
totalIncentive = 0

for presentedOrder in incentive_list:
    if count < 4:
        xpos = -505
    elif count < 8:
        xpos = -90
    else:
        xpos = 345
    
    if count % 4 == 0:
        ypos = 258
    elif count % 4 == 1:
        ypos = 118
    elif count % 4 == 2:
        ypos = -20
    else:
        ypos = -158

    text_incentive = visual.TextStim(win=win,font='Calibri',height=50,color=(-1,-1,-1),colorSpace='rgb',alignText='right')
    text_incentive.text = presentedOrder[-1] #'Round '+str(count+1)+": "+
    text_incentive.pos = (xpos,ypos)
    try:
        totalIncentive += presentedOrder[-1]
        if int(text_incentive.text) < 0:
            text_incentive.color = (0.7020,-1,-1)
        else:
            text_incentive.color = (-1,-1,1)
    except:
        pass

    text_incentive_list.append(text_incentive)
    count+=1

text_totalIncentive = visual.TextStim(text = f'You got {totalIncentive} points',pos=(0,-300) ,win=win,font='Calibri',height=60,color='black',wrapWidth = 500000)

# ------Prepare to start Routine "Incentive"-------
continueRoutine = True
# update component parameters for each repeat
mouse_incentive.clicked_name = []
gotValidClick = False
key_incentive.keys = []
key_incentive.rt = []
_key_incentive_allKeys = []
# keep track of which components have finished
IncentiveComponents = [mouse_incentive,key_incentive,OK_incentive,text_summary,text_totalIncentive,interface_incentive]
IncentiveComponents.extend(text_incentive_list)
for thisComponent in IncentiveComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
IntervalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Incentive"-------
while continueRoutine:
    # get current time
    t = IntervalClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=IntervalClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # # *text_summary* updates
    # if text_summary.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
    #     # keep track of start time/frame for later
    #     text_summary.frameNStart = frameN  # exact frame index
    #     text_summary.tStart = t  # local t and not account for scr refresh
    #     text_summary.tStartRefresh = tThisFlipGlobal  # on global time
    #     win.timeOnFlip(text_summary, 'tStartRefresh')  # time at next scr refresh
    #     text_summary.setAutoDraw(True)

    if interface_incentive.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        interface_incentive.frameNStart = frameN  # exact frame index
        interface_incentive.tStart = t  # local t and not account for scr refresh
        interface_incentive.tStartRefresh = tThisFlipGlobal  # on global time
        # assign lastflip time to tStartRefresh until next flip
        win.timeOnFlip(interface_incentive, 'tStartRefresh')  # time at next scr refresh 
        interface_incentive.setAutoDraw(True)

    # *text_totalIncentive* updates
    if text_totalIncentive.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_totalIncentive.frameNStart = frameN  # exact frame index
        text_totalIncentive.tStart = t  # local t and not account for scr refresh
        text_totalIncentive.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_totalIncentive, 'tStartRefresh')  # time at next scr refresh
        text_totalIncentive.setAutoDraw(True)

    # *text_incentive* updates
    for round in text_incentive_list:
        if round.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            round.frameNStart = frameN  # exact frame index
            round.tStart = t  # local t and not account for scr refresh
            round.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(round, 'tStartRefresh')  # time at next scr refresh
            round.setAutoDraw(True)

    # *OK_incentive* updates
    if OK_incentive.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        OK_incentive.frameNStart = frameN  # exact frame index
        OK_incentive.tStart = t  # local t and not account for scr refresh
        OK_incentive.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(OK_incentive, 'tStartRefresh')  # time at next scr refresh
        OK_incentive.setAutoDraw(True)

    if mouse_incentive.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_incentive.frameNStart = frameN  # exact frame index
        mouse_incentive.tStart = t  # local t and not account for scr refresh
        mouse_incentive.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_incentive, 'tStartRefresh')  # time at next scr refresh
        mouse_incentive.status = STARTED
        mouse_incentive.mouseClock.reset()
        prevButtonState = mouse_incentive.getPressed()  # if button is down already this ISN'T a new click
    if mouse_incentive.status == STARTED:  # only update if started and not finished!
        buttons = mouse_incentive.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [OK_incentive]:
                    if obj.contains(mouse_incentive):
                        gotValidClick = True
                        mouse_incentive.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False    
    # *key_incentive* updates
    waitOnFlip = False
    if key_incentive.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_incentive.frameNStart = frameN  # exact frame index
        key_incentive.tStart = t  # local t and not account for scr refresh
        key_incentive.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_incentive, 'tStartRefresh')  # time at next scr refresh
        key_incentive.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_incentive.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_incentive.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_incentive.status == STARTED and not waitOnFlip:
        theseKeys = key_incentive.getKeys(keyList=['6'], waitRelease=True)
        _key_incentive_allKeys.extend(theseKeys)
        if len(_key_incentive_allKeys):
            key_incentive.keys = _key_incentive_allKeys[-1].name  # just the last key pressed
            key_incentive.rt = _key_incentive_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False

    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IncentiveComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Incentive"-------
for thisComponent in IncentiveComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
        thisComponent.tStopRefresh = tThisFlipGlobal
thisExp.addData('Incentive.started', text_totalIncentive.tStartRefresh)
thisExp.addData('Incentive.stopped', text_totalIncentive.tStopRefresh)
thisExp.addData('totalIncentive', totalIncentive)
print('totalIncentive: ',totalIncentive)

stage2df = stage2df.append({'Round': str(r+1),
                            'Trial': 'Incentive',
                            'Onset': text_totalIncentive.tStartRefresh,
                            'Offset': text_totalIncentive.tStopRefresh}
                            ,ignore_index=True)

routineTimer.reset()




# ------Prepare to start Routine "endExp"-------
continueRoutine = True
# update component parameters for each repeat
mouse_endExp.clicked_name = []
gotValidClick = False
key_endExp.keys = []
key_endExp.rt = []
_key_endExp_allKeys = []

# keep track of which components have finished
endExpComponents = [OK_endExp, mouse_endExp, text_endExp, key_endExp, text_final_reward]
for thisComponent in endExpComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endExpClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1


# -------Run Routine "endExp"-------

all_incentive_rule = {'Behavior':[150, 0.02, 0.01, 0.005, 350], 'MRS-fMRI': [1200, 0.02, 0.01, 0.01, 1450], 'PET-fMRI': [1500, 0.1, 0.1, 0.05, 3000]}
experiment = expInfo['experiment']
current_rule = all_incentive_rule[experiment]

def final_reward_calc(totalIncentive, current_rule):

    base = current_rule[0]
    a_5000 = current_rule[1]
    b_10000 = current_rule[2]
    c_20000 = current_rule[3]
    ceiling = current_rule[4]

    final_reward = 0
    if totalIncentive < 0:
        final_reward = base

    if totalIncentive >= 0 and totalIncentive <= 5000:
        final_reward = totalIncentive * a_5000 + base

    if totalIncentive >= 5001 and totalIncentive <= 10000:
        final_reward = 5000 * a_5000 + (totalIncentive-5000) * b_10000 + base

    if totalIncentive >= 10001 and totalIncentive <= 20000:
        final_reward = 5000 * a_5000 + 5000 * b_10000 + (totalIncentive-10000) * c_20000 + base

    if totalIncentive >= 20000:
        final_reward = ceiling


    return final_reward



final_reward = final_reward_calc(totalIncentive, current_rule)
text_final_reward.text = f"實驗報酬經計算後為：{final_reward}"
    
thisExp.addData('Final reward', final_reward)

while continueRoutine:
    # get current time
    t = endExpClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endExpClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *OK_endExp* updates
    if OK_endExp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        OK_endExp.frameNStart = frameN  # exact frame index
        OK_endExp.tStart = t  # local t and not account for scr refresh
        OK_endExp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(OK_endExp, 'tStartRefresh')  # time at next scr refresh
        OK_endExp.setAutoDraw(True)

    # *text_endExp* updates
    if text_endExp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_endExp.frameNStart = frameN  # exact frame index
        text_endExp.tStart = t  # local t and not account for scr refresh
        text_endExp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_endExp, 'tStartRefresh')  # time at next scr refresh
        text_endExp.setAutoDraw(True)    # *text_endExp* updates

    if text_final_reward.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_final_reward.frameNStart = frameN  # exact frame index
        text_final_reward.tStart = t  # local t and not account for scr refresh
        text_final_reward.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_final_reward, 'tStartRefresh')  # time at next scr refresh
        text_final_reward.setAutoDraw(True)

    if mouse_endExp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_endExp.frameNStart = frameN  # exact frame index
        mouse_endExp.tStart = t  # local t and not account for scr refresh
        mouse_endExp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_endExp, 'tStartRefresh')  # time at next scr refresh
        mouse_endExp.status = STARTED
        mouse_endExp.mouseClock.reset()
        prevButtonState = mouse_endExp.getPressed()  # if button is down already this ISN'T a new click
    if mouse_endExp.status == STARTED:  # only update if started and not finished!
        buttons = mouse_endExp.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [OK_endExp]:
                    if obj.contains(mouse_endExp):
                        gotValidClick = True
                        mouse_endExp.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False    
    # *key_endExp* updates
    waitOnFlip = False
    if key_endExp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_endExp.frameNStart = frameN  # exact frame index
        key_endExp.tStart = t  # local t and not account for scr refresh
        key_endExp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_endExp, 'tStartRefresh')  # time at next scr refresh
        key_endExp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_endExp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_endExp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_endExp.status == STARTED and not waitOnFlip:
        theseKeys = key_endExp.getKeys(keyList=['6'], waitRelease=True)
        _key_endExp_allKeys.extend(theseKeys)
        if len(_key_endExp_allKeys):
            key_endExp.keys = _key_endExp_allKeys[-1].name  # just the last key pressed
            key_endExp.rt = _key_endExp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endExpComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "endExp"-------
for thisComponent in endExpComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
        thisComponent.tStopRefresh = tThisFlipGlobal
        thisExp.addData('text_endExp.started' , text_endExp.tStartRefresh)
        thisExp.addData('text_endExp.stopped' , text_endExp.tStopRefresh)
stage2df = stage2df.append({'Round': str(r+1),
                            'Trial': 'endExp',
                            'Onset': text_endExp.tStartRefresh,
                            'Offset': text_endExp.tStopRefresh}
                            ,ignore_index=True)

# the Routine "endExp" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
stage2df.to_csv(dfname+'.csv',index=False)
win.flip()


# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim=',')
logging.flush()

creds = driveapi.getCreds("driveapi/token.json")
folderid = driveapi.create_folder(expInfo['participant']+'_stage2', creds)
# folderid = driveapi.search_folder('test', creds)[0]['id']
driveapi.upload_to_folder(folderid, filename+'.csv', creds)
driveapi.upload_to_folder(folderid, dfname+'.csv', creds)

# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
          