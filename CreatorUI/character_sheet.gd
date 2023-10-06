extends Control

var dirty=false;


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(_delta):
	pass


func _on_any_text_changed(new_text):
	if(!dirty):
		print("now unsaved")
	dirty=true
