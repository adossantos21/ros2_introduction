# Introduction to ROS 2

Take note of `cheatsheet_ros2.pdf`, since it will be very helpful.

## Installation

Jazzy is the current LTS distro for ROS2. If a new LTS distro is released, chances are it is backwards compatible, meaning you can replace `jazzy` with the name of the new distro `<distro>` in the following steps. For example, replace `sudo apt install ros-jazzy-ros-gz` with `sudo apt install ros-<distro>-ros-gz`.

Dual booting Ubuntu is recommended when operating Gazebo Ionic. These steps assume you have Ubuntu 24.04.3 LTS installed as your OS.

### 1. Install ROS2 Jazzy. 

1. (a) Navigate to `https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html`

   (b) Alternatively, search for `ros2 jazzy install` in your browser and navigate to `deb packages` under Ubuntu Linux.

2. Follow the guidelines for installing ROS2 Jazzy distribution. Opt for the recommended desktop installation and make sure to install the optional development tools.

3. Add the following to the end of your .bashrc

   ```
   export TURTLEBOT3_MODEL=burger # can be burger or waffle
   source /opt/ros/jazzy/setup.bash
   source /path/to/ros2_introduction/install/setup.bash
   ```

### 2. Install git and clone repository.

```
sudo apt install git
git clone git@github.com:adossantos21/ros2_introduction.git
```

### 3. Make `ros2_introduction` your current directory and build the package:

`colcon build --symlink-install`

**${\color{red}Remember \space to \space source \space your \space .bashrc \space after \space building. \space In \space the \space terminal, \space execute \space}$** `source ~/.bashrc` **${\color{red}\space or \space just \space open}$**

**${\color{red}a \space new \space terminal \space and \space run \space your \space nodes \space or \space launch \space files.}$**


### OPTIONAL
If colcon is not recognized, check if you have it installed by running: `sudo apt install python3-colcon-common-extensions`. The optional development tools in ROS2 Jazzy should have installed colcon.
