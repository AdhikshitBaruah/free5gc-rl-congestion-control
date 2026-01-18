# Free5GC RL Congestion Control

This repository implements an RL-based congestion control
framework for Free5GC using three high-impact control parameters:

1. Slice Resource Share
2. 5QI Re-Mapping
3. ARP Bias

## Control Parameters

### Slice Resource Share
Controls how total network capacity is divided across slices.

### 5QI Re-Mapping
Dynamically adjusts QoS class assignments under congestion.

### ARP Bias
Controls which sessions are retained or dropped when resources
are exhausted.

## Goal

This project focuses on **live control**, not prediction:
- Delayed rewards
- Rare congestion events
- Long-horizon memory

Designed for:
- Free5GC simulation
- Offline dataset replay
- Future 5G/6G autonomy research
