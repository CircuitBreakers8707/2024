#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import commands2
import wpilib
import wpilib.drive
import rev

import constants
import math


class DriveSubsystem(commands2.Subsystem):
    def __init__(self) -> None:
        super().__init__()

        self.left1 = rev.CANSparkMax(
            constants.kLeftMotor1Port, rev.CANSparkMax.MotorType.kBrushless
        )
        self.left2 = rev.CANSparkMax(
            constants.kLeftMotor2Port, rev.CANSparkMax.MotorType.kBrushless
        )
        self.right1 = rev.CANSparkMax(
            constants.kRightMotor1Port, rev.CANSparkMax.MotorType.kBrushless
        )
        self.right2 = rev.CANSparkMax(
            constants.kRightMotor2Port, rev.CANSparkMax.MotorType.kBrushless
        )

        # Set current limits for the drivetrain motors
        self.left1.setSmartCurrentLimit(constants.kDTCurrentLimit)
        self.left2.setSmartCurrentLimit(constants.kDTCurrentLimit)
        self.right1.setSmartCurrentLimit(constants.kDTCurrentLimit)
        self.right2.setSmartCurrentLimit(constants.kDTCurrentLimit)

        self.leftDrive = wpilib.MotorControllerGroup(self.left1, self.left2)
        self.rightDrive = wpilib.MotorControllerGroup(self.right1, self.right2)
        #self.leftDrive.setInverted(True)
        #self.rightDrive.setInverted(True)

        # The robot's drive
        self.drive = wpilib.drive.DifferentialDrive(
            self.leftDrive,
            self.rightDrive
        )

    def arcadeDrive(self, fwd: float, rot: float) -> None:
        """
        Drives the robot using arcade controls.

        :param fwd: the commanded forward movement
        :param rot: the commanded rotation
        """
        self.drive.arcadeDrive(0.75 * fwd, -0.5 * rot)
