Subuser - Securing the Linux desktop with Docker
-------------------------------------------------

.. image:: http://subuser.org/_static/images/subuser-logo.png
   :target: http://subuser.org

`Visit us at subuser.org <http://subuser.org>`_

As free software developers we like to share.  We surf the web and discover new code.  We are eager to try it out.  We live out an orgy of love and trust, unafraid that some code we cloned from Git might be faulty or malicious.  We live in the 60s, carefree hippies.

This is utopia.

But sharing code isn't safe.  Every time we try out some stranger's script, we put ourselves at risk.  Despite the occasional claim that Linux is a secure operating system, haphazardly sharing programs is NOT secure.

Furthermore, the fragmentation of the Linux desktop means that packaging work is needlessly repeated.  Programs that build and run on Fedora must be repackaged for Ubuntu.

Subuser with Docker attacks both problems simultaneously.  Docker provides an isolated and consistent environment for your programs to run in.  Subuser gives your desktop programs access to the resources they need in order to function normally.

Subuser turns Docker containers into normal Linux programs:
------------------------------------------------------------

Right now I'm editing this file in ``vim``.  ``vim`` is not installed on my computer though.  It is installed in a docker container.  However, in order to edit this file, all I had to do was type::

    $ vim README.md

Subuser turns a docker container into a normal program.  But this program is not fully privileged.  It can only access the directory from which it was called, `not my entire home dir <http://xkcd.com/1200/>`_.  Each subuser is assigned a specific set of permissions, just like in Android.  You can see an example ``permissions.json`` file bellow.

::

    {
      "description"                : "A web browser."
      ,"maintainer"                : "Timothy Hobbs <timothyhobbs (at) seznam dot cz>"
      ,"executable"                : "/usr/bin/firefox"
      ,"user-dirs"                 : [ "Downloads"]
      ,"gui"                       : {"clipboard":true,"cursors":true}
      ,"sound-card"                : true
      ,"allow-network-access"      : true
    }

For a list of all permissions supported by subuser, please see `the subuser standard <http://subuser.org/subuser-standard/permissions-dot-json-file-format.html>`_.

Installation
------------

System Requirements
--------------------

 * `Docker <http://www.docker.io/gettingstarted/#h_installation>`_ 1.3 or higher

 * Python >= 3

 * Git

 * X11 and the xauth utility (You almost certainly have this)

Install with pip3: Stable version
--------------------------------

1. Add yourself to the `docker group <http://docs.docker.io/en/v0.7.3/use/basics/>`_.

.. note:: Being a member of the ``docker`` group is equivalent to having root access.

::

   $ sudo nano /etc/group

Find ``docker`` and add your username to the end of the line.

2. Install subuser from pip3.

  $ sudo pip3 install subuser

3. Add ``~/.subuser/bin`` to your path by adding the line ``PATH=$HOME/.subuser/bin:$PATH`` to the end of your ``.bashrc`` file.

4. Log out and then back in again.

5. Done!

Install from git: Development version
-------------------------------------

1. Add yourself to the `docker group <http://docs.docker.io/en/v0.7.3/use/basics/>`_.

.. note:: Being a member of the ``docker`` group is equivalent to having root access.

2. Download the subuser repository

  ::

  $ cd
  $ git clone https://github.com/subuser-security/subuser

3. Add ``subuser/logic`` and ``~/.subuser/bin`` to your path by adding the line ``PATH=$HOME/subuser/logic:$HOME/.subuser/bin:$PATH`` to the end of your ``.bashrc`` file.

.. note:: You will need to change the path to ``subuser/logic`` to refer to the location to which you downloaded subuser.

4. Log out and then back in again.

5. Done!

To learn more and read the full manual please visit `subuser.org <http://subuser.org>`_
