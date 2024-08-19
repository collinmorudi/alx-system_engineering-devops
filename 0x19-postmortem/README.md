# Postmortem: The Great Cache Crash of 2024

**Prepared by:** Collin Morudi  
**Date:** August 19, 2024

## Issue Summary
**Duration:** 3 hours 15 minutes (14:00 SAST - 17:15 SAST)  
**Impact:** Our caching service experienced a complete outage, causing significant slowdowns and errors across our web application. Users faced delays in content loading, and approximately 70% of active users were affected, leading to a surge in customer complaints.  
**Root Cause:** An unexpected increase in traffic combined with a misconfigured cache eviction policy led to a complete cache overflow, resulting in service downtime.

## Timeline
- **14:00 SAST** - Monitoring system detects a sudden spike in response times across the web application.
- **14:05 SAST** - Alert triggered, and on-call engineers begin investigating the issue.
- **14:15 SAST** - Initial investigation reveals that the caching layer is unresponsive.
- **14:30 SAST** - Engineers assume the issue may be related to a recent deployment or network issues.
- **14:45 SAST** - Misleading path: Network diagnostics show normal performance, leading to further investigation of the application code.
- **15:00 SAST** - Incident escalated to the infrastructure team for deeper analysis of the caching service.
- **15:30 SAST** - Analysis reveals cache eviction policy misconfiguration and memory overflow.
- **16:00 SAST** - Cache service is manually restarted, but the issue persists due to backlog.
- **16:45 SAST** - Engineers implement a temporary fix by increasing cache memory limits.
- **17:15 SAST** - Normal operation is fully restored after clearing the backlog.

## Root Cause and Resolution
The root cause of the outage stemmed from an unexpected surge in user traffic, which was compounded by a misconfigured cache eviction policy. The policy was set to evict items based on a time-to-live (TTL) that was too long, preventing the cache from clearing out stale data effectively. As a result, the cache became overloaded, leading to unresponsive behavior.

### Resolution Steps:
1. **Identified the Misconfiguration:** Engineers analyzed the cache metrics and found that the eviction policy was not functioning as intended, leading to excessive memory usage.
2. **Increased Cache Memory:** To mitigate the immediate impact, the cache memory limits were temporarily increased, allowing the service to handle the backlog of requests.
3. **Reconfigured Eviction Policy:** The eviction policy was adjusted to a more aggressive setting, allowing stale data to be cleared more frequently, thus preventing future overflows.

## Corrective and Preventative Measures
### Areas for Improvement:
- **Monitoring Enhancements:** Improve monitoring of cache performance metrics to detect potential overflow conditions before they escalate.
- **Configuration Management:** Implement stricter configuration management practices to ensure cache settings are correctly reviewed before deployment.
- **Traffic Management:** Introduce rate-limiting mechanisms to manage sudden spikes in traffic more effectively.

### Specific Tasks:
- **TODO:** Update cache eviction policy to a more aggressive setting.
- **TODO:** Increase cache memory limits permanently based on usage patterns.
- **TODO:** Implement detailed monitoring for cache hit/miss ratios and memory usage.
- **TODO:** Create a runbook for handling cache-related incidents, including procedures for quick recovery.
- **TODO:** Conduct a post-incident review with all involved teams to discuss findings and improvements.

## Conclusion
The Great Cache Crash of 2024 served as a crucial reminder of the importance of robust cache management and monitoring practices. By addressing the identified issues and implementing preventative measures, we aim to enhance system resilience and ensure a smoother experience for our users in the future.

