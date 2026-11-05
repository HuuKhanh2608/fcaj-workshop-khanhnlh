---
title: "Resource cleanup"
date: 2026-11-05
weight: 7
chapter: false
pre: "<b>5.7. </b>"
---

> **Draft in progress.** Content will be updated from Nguyễn Lê Hữu Khánh’s learning, implementation work, and actual supporting evidence.

## Cleanup scope

The actual resource inventory, lab-resource identifiers, and dependency order are pending. The guide will specify account, Region, and stack / name / tag checks before each action.

| Order | Resource | Backup / deletion prerequisites | Command or action | Cleanup verification |
| --- | --- | --- | --- | --- |
| To be defined | Pending | To be defined | Pending | Not performed |

## Supporting resources and storage

Once the architecture is known, check bucket data, object versions, log groups, alarms, snapshots, images, Elastic IPs, endpoints, or retained resources if created by the lab. Identify data to preserve and data that may be deleted.

## Post-cleanup verification

Not performed yet. Evidence will include remaining resources, checks in the correct Region, and a COST review. Any resources intentionally retained will be recorded with their estimated charges.
