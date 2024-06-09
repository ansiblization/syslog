# Ansible role for configuring a syslog service on Debian-based hosts

This role installs and configures a syslog-ng instance on a Debian-based host. It can be included in another role's dependencies to ensure that a proper syslog configuration exists before installing role-specific drop-in configuration files.

The variables that can be used to parametrize the syslog installation, along with their defaults, can be found below:

```yml
syslog_owner: root # The user owning the generated log files and folders
syslog_group: adm # The group owning the generated log files and folders
syslog_dir_mode: "0770" # The ownership mode used for log folders
syslog_file_mode: "0660" # The ownership mode used for log files

syslog_use_fqdn: true # Keep the fully qualified domain name as the hostname in local and remote logs
syslog_use_dns: false # Use DNS reverse-lookup to resolve domain names of log origins
syslog_dns_cache: false # Use DNS cache for domain names of log origins

syslog_network_driver: syslog # The driver to use for network syslog connections. Possible values: `syslog` or `network` (legacy)
syslog_network_source: s_network # The name of the source for network logs (do not change unless you know what you are doing)
syslog_network_destination: d_network # The name of the destination for network logs (do not change unless you know what you are doing)
syslog_local_source: s_src # The name of the source for local logs (do not change unless you know what you are doing)
syslog_local_destination: d_local # The name of the destination for local logs (do not change unless you know what you are doing)

syslog_client_filter_level: null # Only send logs above this level to the remote syslog server, will send all logs if set to `null`
syslog_client_remote_server: null # Hostname or address of a remote syslog server to send logs to, will not connect to a server if set to `null`
syslog_client_transport: tcp # Transport to use for the connection to a remote syslog server. Possible values: `tcp` or `udp`
syslog_client_port: 514 # Remote syslog server port to connect to

syslog_server: false # If set to true, the syslog service will listen for incoming syslog connections from remote clients
syslog_server_tcp: true # Enable listening for TCP connections from remote syslog clients
syslog_server_udp: true # Enable listening for UDP connections from remote syslog clients
syslog_server_address: 0.0.0.0 # Address to listen on for remote connections, will listen on all addresses by default
syslog_server_port_tcp: 514 # Port to listen on for remote TCP connections
syslog_server_port_udp: 514 # Port to listen on for remote UDP connections
syslog_server_create_dirs: true # Automatically create directories for remote syslog clients
syslog_server_directory: /var/log/clients # Path to use to store logs received from remote syslog clients
syslog_server_file: "${HOST}/${FACILITY}.log" # File name format to use for logs from remote syslog clients
syslog_server_max_connections: 500 # Maximum number of simultaneous client connections to the syslog server
syslog_server_keep_hostname: true # Keep hostname for remote syslog client logs

syslog_server_logrotate_schedule: daily # Frequency of remote syslog client log rotation
syslog_server_logrotate_keep: 7 # Amount of old rotated logs to keep
syslog_server_logrotate_date: true # Append the date to rotated log file names
syslog_server_logrotate_create: false # Create new log file after log rotation
syslog_server_logrotate_compress: true # Compress rotated logs
```
