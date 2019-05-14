robot-framework-percy
=====================

.. contents::

Introduction
------------
Robot framework client library for visual regression testing with Percy.

Installation
------------

The recommended installation method is using pip::

    pip install robot-framework-percy

Usage
-----

.. code:: robotframework

    *** Settings ***
    Library    RobotFrameworkPercy


    *** Keywords ***
    Initialize
        Open Browser              url    Chrome

        # initialize percy
        Percy Initialize Build    access_token=${PERCY_TOKEN}

    Take Snapshot
        # take snapshot
        Percy Snapshot    snapshot name

    Teardown
        # finalize and push to percy server
        Percy Finalize Build

