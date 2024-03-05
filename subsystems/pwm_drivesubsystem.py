#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import commands2
import wpilib
import wpilib.drive

import constants


class DriveSubsystem(commands2.Subsystem):
    def __init__(self) -> None:
        super().__init__()

        self.left1 = wpilib.PWMSparkMax(constants.kLeftMotor1Port)
        self.left2 = wpilib.PWMSparkMax(constants.kLeftMotor2Port)
        self.right1 = wpilib.PWMSparkMax(constants.kRightMotor1Port)
        self.right2 = wpilib.PWMSparkMax(constants.kRightMotor2Port)

        self.leftDrive = wpilib.MotorControllerGroup(self.left1, self.left2)
        self.rightDrive = wpilib.MotorControllerGroup(self.right1, self.right2)
        self.leftDrive.setInverted(True)

        # The robot's drive
        self.drive = wpilib.drive.DifferentialDrive(
            self.leftDrive,
            self.rightDrive,
        )

    def arcadeDrive(self, fwd: float, rot: float) -> None:
        """
        Drives the robot using arcade controls.

        :param fwd: the commanded forward movement
        :param rot: the commanded rotation
        """
        self.drive.arcadeDrive(fwd, rot)
