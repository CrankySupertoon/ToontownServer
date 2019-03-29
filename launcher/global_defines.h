/*
 * Created by Joshua Synder
 * Modified for the useage of the TT Revision project
 *
*/


#ifndef GLOBALDEFINES_H
#define GLOBALDEFINES_H

#endif // GLOBALDEFINES_H

//Platform Specific Configurations
#ifdef Q_OS_LINUX
#define DEFAULT_PATH QDir::homePath() + QString("/Toontown_Server")
#define PLATFORM    "linux2"
#define ENGINE_FILENAME QString("./start_game")

//for windows support (should now work)
#elif defined(Q_OS_WIN)
#define DEFAULT_PATH QString(QDir::currentPath()) + QString("/Game-Files")
#define ENGINE_FILENAME QString("start_game.bat")
#define PLATFORM    "win32"

//For OS X support (not used because no mac to compile and test on)
#elif defined(Q_OS_MAC)
#define DEFAULT_PATH QDir::homePath() + QString("/Library/Application Support/Toontown_Server")
#define LIBRARY_PATH QString("./Libraries.bundle")
#define ENGINE_FILENAME QString("\"./Toontown Rewritten\"")
#define PLATFORM "darwin"

#else
#endif


