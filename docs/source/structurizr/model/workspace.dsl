/*
  bioterm Architecture
*/

/* Constant values */
!constant ORGANISATION_NAME "bioterm"
!constant GROUP_NAME "bioterm"

workspace "Setup" "bioterm Services"  {

  model {
#     bioterm = enterprise "${ORGANISATION_NAME} - ${GROUP_NAME}" {

      user = person "User"
      admin = person "Admin"

      serialDeviceSystem = softwareSystem "Lab Device connected to Controller" {
            serialDeviceFirmware = container "Lab Device Firmware"
      }

      serialDeviceSystem2 = softwareSystem "Lab Device connected to Gateway" {
            serialDeviceFirmware2 = container "Lab Device Firmware 2"
      }

      teleportSystem = softwareSystem "Access Proxy System" {
            teleport = container "Teleport Server"
      }

      saadSystem = softwareSystem "Software as a Device" {
            saadContainer = container "Software as a Device"
      }

      biotermServer = softwareSystem "bioterm Server System" {
            group "Dockerized (Docker Compose)"  {
                  api = container "bioterm API" "bioterm Backend API" "Python/FastAPI" "python"
                  pwa = container "bioterm Web App" "User interface" "HTML/Typescript/Vue/Quasar" "quasar"
                  /* webApplication = container "Web Server" "Delivers the bioterm progressive web app" "NPM HTTPS Server" */
                  grafana = container "Grafana" "Provides visualization" "grafana" "grafana"
                  redis = container "Redis" "Interprocess Communication" "redis" "redis"
                  postgreSQL = container "SQL Database" "Stores application and device data" "PostgreSQL/TimescaleDB" "postgresql"
                  databaseWorker = container "Database Worker" "Writes device data to database" "Python" "python"
                  identityProvider = container "Identity Provider" "Manages authentication and issues JWT" "Authentik" "authentik"
                  eln = container "eLabFTW" "Electronic Lab Notebook" "eLabFTW" "elabftw"
            }

      }

      biotermController = softwareSystem "bioterm Controller(s)" {
            group "Dockerized (Docker Compose)"  {
                  redisController = container "Redis" "Pub/Sub, Redis Streams, In-Memory DB" "redis" "redis"
                  registrationService = container "Registration Service" "" "Python"
                  websocketWorker = container "Websocket Worker" "Tunnels data packages to/from server" "python"
                  centralControl = container "State Management / Control Process" "Evaluates datapoints and RPCs" "python"
            }
            /* biotermDeviceAdapter1 = container "bioterm Device Adapter" "" "Python" */
            /* deviceDriverSerialDeviceOnController = container "Device Driver for Serial Device" "" "Python" */
      }



      biotermDeviceGateway = softwareSystem "bioterm Device Gateway" {
            biotermDeviceAdapter2 = container "bioterm Device Adapter" "" "Python"
            deviceDriverSerialDeviceOnGateway = container "Device Driver for Serial Device" "" "Python"
      }

      biotermDeviceDriver = softwareSystem "bioterm Device System" {
            deviceDriver = container "bioterm Device Driver" {
                  deviceAdapterComponent = component "bioterm Device Adapter" "" "" "Python"
                  deviceDriverComponent = component "Device Driver" "" "" "Python"
            }
      }

      biotermDevice = softwareSystem "bioterm Device Process" {
             deviceManager = container "Device Manager" "" "" "Python"
      }

      backupSystem = softwareSystem "backup" {
            backupContainer = container "backup"
      }


      biotermDevice -> biotermController "Communicates with" "TCP"
      saadSystem -> biotermController "Communicates with" "TCP"

      registrationService -> redisController "Communicates with" "TCP"
      websocketWorker -> redisController "Communicates with" "TCP"
      biotermDevice -> redisController "Communicates with" "TCP"
      /* deviceDriverSerialDeviceOnController -> biotermDeviceAdapter1 "Uses" */
      /* deviceDriverSerialDeviceOnController -> serialDeviceSystem "Controls" "RS232/RS485/USB" */
      /* biotermDeviceAdapter1 -> redisController "Sends device registration and datapoints, checks for RPCs" */
      /* biotermDeviceAdapter2 -> redisController "Sends device registration and datapoints, checks for RPCs" */
      centralControl -> redisController "Communicates with" "TCP"

      deviceDriverSerialDeviceOnGateway -> serialDeviceSystem2 "Controls" "RS232/RS485/USB"

      pwa -> api "Connects to" "JSON/HTTPS"
      api -> grafana "Connects to" "JSON/HTTPS"
      api -> eln "Connects to" "JSON/HTTPS"
      api -> redis "Reads/Writes" "TCP"
      api -> postgreSQL "Reads/Writes" "TCP"
      databaseWorker -> redis "Reads" "TCP"
      databaseWorker -> postgreSQL "Writes" "TCP"
      identityProvider -> pwa "Provides oAuth2 authentication for bioterm API" "HTTPS"
      identityProvider -> grafana "Provides oAuth2 authentication" "HTTPS"
      identityProvider -> eln "Provides SAML authentication" "HTTPS"
      registrationService -> api "Registers controller and devices" "HTTPS"
      websocketWorker -> api "Initiates bidirectional communication" "WSS"

      grafana -> pwa "Provides device visualization to" "iframe/HTTPS"
      grafana -> postgreSQL "Reads" "TCP"

      admin -> teleportSystem "Uses"
      user -> pwa "Uses"
      user -> eln "Uses"
      user -> identityProvider "Uses"
      /* identityProvider -> user "Returns JWT" */
      /* identityProvider -> admin "Returns JWT" */



#     }

  /* Deployment / Infrastructure */
      production = deploymentEnvironment "Production" {
            deploymentNode "bioterm Data Center" {
                  deploymentNode "High Availability Server Cluster" "" "Proxmox" {
                        biotermVM = deploymentNode "Virtual Machine" "" "Ubuntu 22.04" {
                              softwareSystemInstance biotermServer
                              #  containerInstance api
                        }
                        backupVM = infrastructureNode "Backup Storage VM" "" "Ubuntu 22.04"
                  }
                  infrastructureNode "VM Backup Server" "" "Proxmox"
                  # biotermFirewall = infrastructureNode "Firewall and Router" "" "pfSense"

            }
            # deploymentNode "Cloud Server" {
            #     containerInstance api
            # }
            deploymentNode "Externally Managed Network" {
                  deploymentNode "bioterm Controller" {
                        biotermControllerInstance = softwareSystemInstance biotermController
                        deviceOnControllerInstance1 = softwareSystemInstance biotermDevice
                        deviceOnControllerInstance2 = softwareSystemInstance biotermDevice
                        # containerInstance redisController
                        # containerInstance registrationService
                        # containerInstance websocketWorker
                        # containerInstance accessProxyClient
                  }
                  deploymentNode "Local GPU Server" {
                        softwareSystemInstance saadSystem
                  }
                  # deploymentNode "biotermDevice" {
                  #       softwareSystemInstance biotermDevice
                  # }
                  deploymentNode "bioterm Gateway" {
                        deviceOnGatewayInstance = softwareSystemInstance biotermDevice
                  }
                  serialDevice1 = infrastructureNode "Lab Device with Serial Communication"
                  serialDevice2 = infrastructureNode "Lab Device with Serial Communication 2"
                  networkDevice = infrastructureNode "Lab Device with Networked Communication"
                  # otherFirewall = infrastructureNode "Externally Managed Firewall and Router"

            }

        }


      deviceOnControllerInstance1 -> networkDevice "Controls" "Ethernet/Wifi"
      deviceOnControllerInstance2 -> serialDevice2 "Controls" "RS232/RS285/USB"
      deviceOnGatewayInstance -> serialDevice1 "Controls" "RS232/RS285/USB"
      # otherFirewall -> biotermFirewall "Allows outgoing connections on port 443 to"
      # biotermFirewall -> biotermVM "Test"

 /* End Of Production Deployment Environment */

  }
  views {
   /* Overall system */
   systemLandscape {
    include *
    autoLayout lr
   }
   deployment * production {
            include *
        }
    systemContext biotermServer {
      include *
      autoLayout
    }
    container biotermServer serverView "Complete Server view" {
        include *
        include user
    }
    container biotermController controllerView "Complete Controller view" {
        include *
    }

    /* Theme for views */
    themes default https://raw.githubusercontent.com/nilssta/structurizr_theme/main/themes/bioterm.json

  }
}
