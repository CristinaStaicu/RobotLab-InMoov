# -- coding: utf-8 --
def muscle():
  i01.startedGesture()
  i01.setHandVelocity("left", -1, -1, -1, -1, -1, -1)
  i01.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
  i01.setArmVelocity("right", 31.0, 43.0, 59, 43.0)
  i01.setArmVelocity("left", 31.0, 43.0, 59, 43.0)
  i01.setHeadVelocity(22.0, 22.0)
  i01.setTorsoVelocity(31.0, 13.0, -1)
  i01.moveHead(90,129)
  i01.moveArm("left",90,139,48,75)
  i01.moveArm("right",71,40,14,43)
  i01.moveHand("left",180,180,180,180,180,148)
  i01.moveHand("right",99,130,152,154,145,180)
  i01.moveTorso(120,100,90)
  sleep(4)
  i01.mouth.speakBlocking("Looks good, doesn't it")
  #i01.mouth.speakBlocking(u"Выглядит хорошо, не так ли?")
  sleep(2)
  i01.setHandVelocity("left", -1, -1, -1, -1, -1, -1)
  i01.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
  i01.setArmVelocity("right", -1.0, -1.0, -1.0, -1.0)
  i01.setArmVelocity("left", -1.0, -1.0, -1.0, -1.0)
  i01.setHeadVelocity(43.0, 43.0)
  i01.setTorsoVelocity(31.0, 13.0, -1)
  i01.moveHead(90,45)
  i01.moveArm("left",44,46,20,39)
  i01.moveArm("right",90,145,58,74)
  i01.moveHand("left",180,180,180,180,180,83)
  i01.moveHand("right",99,130,152,154,145,21)
  i01.moveTorso(60,75,90)
  sleep(3)
  i01.mouth.speakBlocking("not bad either, don't you think")
  #i01.mouth.speakBlocking(u"Неплохо, не так ли?")
  sleep(4)
  i01.finishedGesture()
  relax()
  sleep(1)
