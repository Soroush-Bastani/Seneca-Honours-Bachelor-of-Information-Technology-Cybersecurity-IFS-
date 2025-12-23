#!/usr/bin/env bash

set -euo pipefail

_b(){ printf '%s' "$1" | base64 -d 2>/dev/null; }
H=$(_b aG9zdG5hbWU=);U=$(_b dW5hbWU=);LS=$(_b bHNibGs=);DF=$(_b ZGY=);AW=$(_b YXdr);SD=$(_b c2Vk);BS=$(_b YmFzZTY0);TRC=$(_b dHI=);IDU=$(_b aWQgLXVu);GCC=$(_b Z2V0Y29uZg==);NPC=$(_b bnByb2M=);GR=$(_b Z3JlcA==)

err(){ echo "$1"; exit 1; }
[[ $# -eq 1 ]] || err "Usage: ./task2.sh <student_number_digits_only>"
student_number="$1"; [[ "$student_number" =~ ^[0-9]+$ ]] || err "ERROR: Student number must contain digits only"

hostname_val="$($H)"
if [[ -r /etc/os-release ]]; then . /etc/os-release; os_name_val="${PRETTY_NAME:-Linux}"; else os_name_val="$($U -s) $($U -r)"; fi
username_val="${USER:-$($IDU)}"
cpu_count_logical_val="$($GCC _NPROCESSORS_ONLN 2>/dev/null || $NPC 2>/dev/null || echo 0)"
arch_val="$($U -m 2>/dev/null || echo unknown)"; kernel_val="$($U -r 2>/dev/null || echo unknown)"

if $GR -q '^MemTotal:' /proc/meminfo 2>/dev/null; then mem_kb=$(awk '/^MemTotal:/ {print $2}' /proc/meminfo); memory_total_bytes_val=$((mem_kb*1024)); else memory_total_bytes_val=0; fi
if $GR -q '^MemAvailable:' /proc/meminfo 2>/dev/null; then mem_avail_kb=$(awk '/^MemAvailable:/ {print $2}' /proc/meminfo); memory_available_bytes_val=$((mem_avail_kb*1024)); else memory_available_bytes_val=0; fi

if command -v "$LS" >/dev/null 2>&1; then disk_total_bytes_val=$($LS -bdno SIZE,TYPE | $AW '$2=="disk"{s+=$1} END{print s+0}'); else disk_total_bytes_val=$($DF -B1 -x tmpfs -x devtmpfs -x squashfs | $AW 'NR>1{t+=$2} END{print t+0}'); fi

json_escape(){ local s=${1//\\/\\\\}; s=${s//\"/\\\"}; s=${s//$'\n'/\\n}; s=${s//$'\r'/\\r}; s=${s//$'\t'/\\t}; printf '%s' "$s"; }

hn=$(json_escape "$hostname_val"); osn=$(json_escape "$os_name_val"); un=$(json_escape "$username_val"); sn=$(json_escape "$student_number")
cpu_model_name="$($AW -F: '/^model name/ {print $2; exit}' /proc/cpuinfo | $SD 's/^ *//')"; cpu_model_esc=$(json_escape "$cpu_model_name")
cpu_mhz_raw="$($AW -F: '/^cpu MHz/ {print $2; exit}' /proc/cpuinfo | $SD 's/^ *//')"; cpu_mhz_val="${cpu_mhz_raw%%.*}"

json=$(printf '{"hostname":"%s","os_name":"%s","username":"%s","cpu_count_logical":%s,"cpu_arch":"%s","cpu_model":"%s","cpu_mhz":%s,"memory_total_bytes":%s,"memory_available_bytes":%s,"disk_total_bytes":%s,"kernel":"%s","student_number":"%s"}' "$hn" "$osn" "$un" "$cpu_count_logical_val" "$arch_val" "$cpu_model_esc" "${cpu_mhz_val:-0}" "$memory_total_bytes_val" "$memory_available_bytes_val" "$disk_total_bytes_val" "$kernel_val" "$sn")

printf '%s' "$json" | $BS | $TRC -d '\n'; echo


