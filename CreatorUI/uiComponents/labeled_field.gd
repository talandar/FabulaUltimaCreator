extends HBoxContainer

onready var _label := $Label

export(String) var label setget _set_label, _get_label

func _set_label(value):
	_label.text = value
	
func _get_label():
	return label

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
