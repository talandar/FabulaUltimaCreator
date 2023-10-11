extends PanelContainer

@onready var base_dex = $MarginContainer/AttributesBox/AttributeAlignment/AttrBaseValues/BaseDEX
@onready var base_ins = $MarginContainer/AttributesBox/AttributeAlignment/AttrBaseValues/BaseINS
@onready var base_mig = $MarginContainer/AttributesBox/AttributeAlignment/AttrBaseValues/BaseMIG
@onready var base_wil = $MarginContainer/AttributesBox/AttributeAlignment/AttrBaseValues/BaseWIL

@onready var tmp_dex = $MarginContainer/AttributesBox/AttributeAlignment/AttrTmpValues/TmpDEX
@onready var tmp_ins = $MarginContainer/AttributesBox/AttributeAlignment/AttrTmpValues/TmpINS
@onready var tmp_mig = $MarginContainer/AttributesBox/AttributeAlignment/AttrTmpValues/TmpMIG
@onready var tmp_wil = $MarginContainer/AttributesBox/AttributeAlignment/AttrTmpValues/TmpWIL

@onready var status_slow = $MarginContainer/AttributesBox/AttributeAlignment/StatusEffectsLight/SlowChk
@onready var status_daze = $MarginContainer/AttributesBox/AttributeAlignment/StatusEffectsLight/DazedChk
@onready var status_weak = $MarginContainer/AttributesBox/AttributeAlignment/StatusEffectsLight/WeakChk
@onready var status_shaken = $MarginContainer/AttributesBox/AttributeAlignment/StatusEffectsLight/ShakenChk

@onready var status_enraged = $MarginContainer/AttributesBox/AttributeAlignment/StatusEffectsHeavy/EnragedChk
@onready var status_poisoned = $MarginContainer/AttributesBox/AttributeAlignment/StatusEffectsHeavy/PoisonedChk


func export():
	var dict = {
		"dex": base_dex.text,
		"ins": base_ins.text,
		"mig": base_mig.text,
		"wil": base_wil.text,
		"tmp_dex": tmp_dex.text,
		"tmp_ins": tmp_ins.text,
		"tmp_mig": tmp_mig.text,
		"tmp_wil": tmp_wil.text,
		"status_slow": status_slow.button_pressed,
		"status_daze": status_daze.button_pressed,
		"status_weak": status_weak.button_pressed,
		"status_shaken": status_shaken.button_pressed,
		"status_enraged": status_enraged.button_pressed,
		"status_poisoned": status_poisoned.button_pressed
	}
	return dict
