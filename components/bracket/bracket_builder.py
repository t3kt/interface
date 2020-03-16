def onCook(dat):
	dat.clear()
	dat.appendRow(['tx', 'ty'])
	inclArm1 = parent().par.Enablearm1
	inclArm2 = parent().par.Enablearm2
	armLen1 = op('length')['arm1']
	armLen2 = op('length')['arm2']
	halfMainLen = op('length')['halfmain']
	mainThick = op('thick')['main']
	armThick1 = op('thick')['arm1']
	armThick2 = op('thick')['arm2']
	armOffset1 = op('offset')['arm1']
	armOffset2 = op('offset')['arm2']
	if inclArm1:
		dat.appendRow([
			0,
			halfMainLen - armOffset1
		])
		dat.appendRow([
			armLen1 + mainThick,
			halfMainLen
		])
		dat.appendRow([
			armLen1 + mainThick,
			halfMainLen - armThick1
		])
		dat.appendRow([
			mainThick,
			halfMainLen - armThick1 - armOffset1
		])
	else:
		dat.appendRow([
			0,
			halfMainLen
		])
		dat.appendRow([
			mainThick,
			halfMainLen
		])
	if inclArm2:
		dat.appendRow([
			mainThick,
			-halfMainLen + armThick2 + armOffset2
		])
		dat.appendRow([
			mainThick + armLen2,
			-halfMainLen + armThick2
		])
		dat.appendRow([
			mainThick + armLen2,
			-halfMainLen
		])
		dat.appendRow([
			0,
			-halfMainLen + armOffset2
		])
	else:
		dat.appendRow([
			mainThick,
			-halfMainLen
		])
		dat.appendRow([
			0,
			-halfMainLen
		])
