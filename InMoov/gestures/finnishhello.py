def finnishhello():
  i01.setHandSpeed("left", 0.60, 0.60, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.65, 0.75)
  i01.moveHead(105,78)
  i01.moveArm("left",78,48,37,11)
  i01.moveArm("right",90,144,60,75)
  i01.moveHand("left",112,111,105,102,81,10)
  i01.moveHand("right",0,0,0,50,82,180)
  sleep(1)

  for w in range(0,3):
    i01.setHandSpeed("left", 0.60, 0.60, 1.0, 1.0, 1.0, 1.0)
    i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 0.60)
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("right", 0.60, 1.0, 1.0, 1.0)
    i01.setHeadSpeed(0.65, 0.75)
    i01.moveHead(83,98)
    i01.moveArm("left",78,48,37,11)
    i01.moveArm("right",90,157,47,75)
    i01.moveHand("left",112,111,105,102,81,10)
    i01.moveHand("right",3,0,62,41,117,94)


    if w==1:
        i01.setHandSpeed("left", 0.60, 0.60, 1.0, 1.0, 1.0, 1.0)
        i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 0.60)
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
        i01.setArmSpeed("right", 0.65, 1.0, 1.0, 1.0)
        i01.setHeadSpeed(0.65, 0.75)
        i01.moveHead(83,70)
        i01.mouth.speakBlocking("hei, nimeni on inmoov")
        i01.moveArm("left",78,48,37,11)
        i01.moveArm("right",57,145,50,68)
        i01.moveHand("left",100,90,85,80,71,15)
        i01.moveHand("right",3,0,31,12,26,45)
        sleep(1)
        i01.moveHead(83,98)
        i01.moveArm("left",78,48,37,11)
        i01.moveArm("right",90,157,47,75)
        i01.moveHand("left",112,111,105,102,81,10)
        i01.moveHand("right",3,0,62,41,117,94)
        sleep(1)
        i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
        i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
        i01.setArmSpeed("right", 0.75, 0.85, 0.95, 0.85)
        i01.setArmSpeed("left", 0.95, 0.65, 0.75, 0.75)
        i01.setHeadSpeed(0.75, 0.75)
        i01.moveHead(79,100)
        i01.moveArm("left",5,94,28,15)
        i01.moveArm("right",5,82,28,15)
        i01.moveHand("left",42,58,42,55,71,35)
        i01.moveHand("right",81,50,82,60,105,113)