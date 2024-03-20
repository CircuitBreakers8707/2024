#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import commands2
import constants

from subsystems.can_drivesubsystem import DriveSubsystem
from subsystems.can_launchersubsystem import LauncherSubsystem
# from subsystems.pwm_drivesubsystem import DriveSubsystem


class Autos(commands2.Command):
    def __init__(self, drive: DriveSubsystem, launcher: LauncherSubsystem) -> None:
        super().__init__()
        self.drive = drive
        self.launcher = launcher
        self.addRequirements(drive)

    def exampleAuto(self) -> commands2.Command:
        return (
    
            
            )
        
