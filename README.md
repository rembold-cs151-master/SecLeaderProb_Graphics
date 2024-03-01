# Miniature Golf
Your task here is to recreate a very basic implementation of miniature golf. The starting template lays out some starting elements and provides one convenience function to you. You need to add functionality such that:

* When the mouse is pressed down, the power bar starts building across the bottom of the screen.
* When the mouse is released, the ball moves towards the mouse location at that point in time with a speed contingent on the power bar. The power bar should be reset during this to prep for the next shot.
* The ball slows over time owing to friction, and bounces off the sides of the map. If the ball starts moving too slowly, stop it and wait for the player to take another shot.
* If the ball reaches a close proximity with the hole and is traveling slow enough, the shot is made! Reset the ball location and randomize the hole location again to start anew!
