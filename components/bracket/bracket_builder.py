def onSetupParameters(dat):
	page = dat.appendCustomPage('Custom')
	page.appendPar('Geomode', par=parent().par.Geomode)
	for name in ['Enablearm1', 'Enablearm2']:
		page.appendToggle(name)
	for name in [
		'Armlength1', 'Armlength2', 'Mainlength',
		'Mainthick', 'Armthick1', 'Armthick2',
		'Armoffset1', 'Armoffset2',
	]:
		page.appendFloat(name)

def onCook(dat):
	mode = dat.par.Geomode
	inclArm1 = dat.par.Enablearm1
	inclArm2 = dat.par.Enablearm2
	armLen1 = dat.par.Armlength1
	armLen2 = dat.par.Armlength2
	halfMainLen = dat.par.Mainlength / 2
	mainThick = dat.par.Mainthick
	armThick1 = dat.par.Armthick1
	armThick2 = dat.par.Armthick2
	armOffset1 = dat.par.Armoffset1
	armOffset2 = dat.par.Armoffset2
	dat.clear()
	dat.appendRow(['tx', 'ty'])
	if mode == 'line':
		if inclArm1:
			dat.appendRow([armLen1, halfMainLen])
			dat.appendRow([0, halfMainLen - armOffset1])
		else:
			dat.appendRow([0, halfMainLen])
		if inclArm2:
			dat.appendRow([0, -halfMainLen + armOffset2])
			dat.appendRow([armLen2, -halfMainLen])
		else:
			dat.appendRow([0, -halfMainLen])
	else:
		if inclArm1:
			dat.appendRow([0, halfMainLen - armOffset1])
			dat.appendRow([armLen1 + mainThick, halfMainLen])
			dat.appendRow([armLen1 + mainThick, halfMainLen - armThick1])
			dat.appendRow([mainThick, halfMainLen - armThick1 - armOffset1])
		else:
			dat.appendRow([0, halfMainLen])
			dat.appendRow([mainThick, halfMainLen])
		if inclArm2:
			dat.appendRow([mainThick, -halfMainLen + armThick2 + armOffset2])
			dat.appendRow([mainThick + armLen2, -halfMainLen + armThick2])
			dat.appendRow([mainThick + armLen2, -halfMainLen])
			dat.appendRow([0, -halfMainLen + armOffset2])
		else:
			dat.appendRow([mainThick, -halfMainLen])
			dat.appendRow([0, -halfMainLen])
