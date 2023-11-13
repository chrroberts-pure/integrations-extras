METRIC_MAP = [
    {
        # shared metrics
        "purefa_info": {"name": "info"},
        "purefa_array_performance_latency_usec": {
            "name": "array.performance_latency_usec"
        },
        "purefa_array_performance_bandwidth_bytes": {
            "name": "array.performance_bandwidth_bytes"
        },
        "purefa_host_performance_latency_usec": {
            "name": "host.performance_latency_usec"
        },
        "purefa_host_performance_bandwidth_bytes": {
            "name": "host.performance_bandwidth_bytes"
        },
        "purefa_host_space_bytes": {"name": "host.space_bytes"},
        "purefa_pod_performance_latency_usec": {"name": "pod.performance_latency_usec"},
        "purefa_pod_performance_bandwidth_bytes": {
            "name": "pod.performance_bandwidth_bytes"
        },
        "purefa_pod_space_bytes": {"name": "pod.space_bytes"},
        "purefa_volume_performance_latency_usec": {
            "name": "volume.performance_latency_usec"
        },
        "purefa_volume_space_bytes": {"name": "volume.space_bytes"},
        # pure-fa-openmetrics-exporter only metrics
        "purefa_alerts_open": {"name": "alerts.open"},
        "purefa_array_performance_average_bytes": {
            "name": "array.performance_average_bytes"
        },
        "purefa_array_performance_queue_depth_ops": {
            "name": "array.performance_queue_depth_ops"
        },
        "purefa_array_performance_throughput_iops": {
            "name": "array.performance_throughput_iops"
        },
        "purefa_array_space_bytes": {"name": "array.space_bytes"},
        "purefa_array_space_data_reduction_ratio": {
            "name": "array.space_data_reduction_ratio"
        },
        "purefa_array_space_utilization": {"name": "array.space_utilization"},
        "purefa_directory_performance_average_bytes": {
            "name": "directory.performance_average_bytes"
        },
        "purefa_directory_performance_bandwidth_bytes": {
            "name": "directory.performance_bandwidth_bytes"
        },
        "purefa_directory_performance_latency_usec": {
            "name": "directory.performance_latency_usec"
        },
        "purefa_directory_performance_throughput_iops": {
            "name": "directory.performance_throughput_iops"
        },
        "purefa_directory_space_bytes": {"name": "directory.space_bytes"},
        "purefa_directory_space_data_reduction_ratio": {
            "name": "directory.space_data_reduction_ratio"
        },
        "purefa_drive_capacity_bytes": {"name": "drive.capacity_bytes"},
        "purefa_host_connections_info": {"name": "host.connections_info"},
        "purefa_host_connectivity_info": {"name": "host.connectivity_info"},
        "purefa_host_performance_average_bytes": {
            "name": "host.performance_average_bytes"
        },
        "purefa_host_performance_throughput_iops": {
            "name": "host.performance_throughput_iops"
        },
        "purefa_host_space_data_reduction_ratio": {
            "name": "host.space_data_reduction_ratio"
        },
        "purefa_hw_component_status": {"name": "hw.component_status"},
        "purefa_hw_component_temperature_celsius": {
            "name": "hw.component_temperature_celsius"
        },
        "purefa_hw_component_voltage_volt": {"name": "hw.component_voltage_volt"},
        "purefa_network_interface_performance_bandwidth_bytes": {
            "name": "network.interface_performance_bandwidth_bytes"
        },
        "purefa_network_interface_performance_errors": {
            "name": "network.interface_performance_errors"
        },
        "purefa_network_interface_performance_throughput_pkts": {
            "name": "network.interface_performance_throughput_pkts"
        },
        "purefa_pod_performance_average_bytes": {
            "name": "pod.performance_average_bytes"
        },
        "purefa_pod_performance_replication_bandwidth_bytes": {
            "name": "pod.performance_replication_bandwidth_bytes"
        },
        "purefa_pod_performance_throughput_iops": {
            "name": "pod.performance_throughput_iops"
        },
        "purefa_pod_replica_links_lag_average_sec": {
            "name": "pod.replica_links_lag_average_sec"
        },
        "purefa_pod_replica_links_lag_max_sec": {
            "name": "pod.replica_links_lag_max_sec"
        },
        "purefa_pod_replica_links_performance_bandwidth_bytes": {
            "name": "pod.replica_links_performance_bandwidth_bytes"
        },
        "purefa_pod_space_data_reduction_ratio": {
            "name": "pod.space_data_reduction_ratio"
        },
        "purefa_volume_performance_average_bytes": {
            "name": "volume.performance_average_bytes"
        },
        "purefa_volume_performance_bandwidth_bytes": {
            "name": "volume.performance_bandwidth_bytes"
        },
        "purefa_volume_performance_throughput_iops": {
            "name": "volume.performance_throughput_iops"
        },
        "purefa_volume_space_data_reduction_ratio": {
            "name": "volume.space_data_reduction_ratio"
        },
        # legacy pure_exporter only metrics
        "purefa_hardware_chassis_health": {"name": "hardware.chassis_health"},
        "purefa_hardware_controller_health": {"name": "hardware.controller_health"},
        "purefa_hardware_component_health": {"name": "hardware.component_health"},
        "purefa_hardware_temperature_celsius": {"name": "hardware.temperature_celsius"},
        "purefa_hardware_power_volts": {"name": "hardware.power_volts"},
        "purefa_alerts_total": {"name": "alerts.total"},
        "purefa_array_space_datareduction_ratio": {
            "name": "array.space_datareduction_ratio"
        },
        "purefa_array_space_capacity_bytes": {"name": "array.space_capacity_bytes"},
        "purefa_array_space_provisioned_bytes": {
            "name": "array.space_provisioned_bytes"
        },
        "purefa_array_space_used_bytes": {"name": "array.space_used_bytes"},
        "purefa_array_performance_iops": {"name": "array.performance_iops"},
        "purefa_array_performance_avg_block_bytes": {
            "name": "array.performance_avg_block_bytes"
        },
        "purefa_array_performance_qdepth": {"name": "array.performance_qdepth"},
        "purefa_host_performance_iops": {"name": "host.performance_iops"},
        "purefa_host_space_datareduction_ratio": {
            "name": "host.space_datareduction_ratio"
        },
        "purefa_host_space_size_bytes": {"name": "host.space_size_bytes"},
        "purefa_pod_mediator_status": {"name": "pod.mediator_status"},
        "purefa_pod_performance_iops": {"name": "pod.performance_iops"},
        "purefa_pod_space_datareduction_ratio": {
            "name": "pod.space_datareduction_ratio"
        },
        "purefa_pod_space_size_bytes": {"name": "pod.space_size_bytes"},
        "purefa_pod_status": {"name": "pod.status"},
        "purefa_volume_performance_iops": {"name": "volume.performance_iops"},
        "purefa_volume_performance_throughput_bytes": {
            "name": "volume.performance_throughput_bytes"
        },
        "purefa_volume_space_datareduction_ratio": {
            "name": "volume.space_datareduction_ratio"
        },
        "purefa_volume_space_size_bytes": {"name": "volume.space_size_bytes"},
    }
]
