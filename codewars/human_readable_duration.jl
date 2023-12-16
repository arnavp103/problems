
# If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.
# For seconds = 3662, your function should return
#     "1 hour, 1 minute and 2 seconds"


function formatduration(seconds)
    if seconds == 0
        return "now"
    end
    minutes, seconds = divrem(seconds, 60)
    hours, minutes = divrem(minutes, 60)
    days, hours = divrem(hours, 24)
    years, days = divrem(days, 365)

    first = true
    # we use and once then commas for the rest
    and = true
    # work backwards
    duration = ""
    if seconds > 0
        duration, first, and = output(duration, first, and, "second", seconds)
    end
    if minutes > 0
        duration, first, and = output(duration, first, and, "minute", minutes)
    end
    if hours > 0
        duration, first, and = output(duration, first, and, "hour", hours)
    end
    if days > 0
        duration, first, and = output(duration, first, and, "day", days)
    end
    if years > 0
        duration, first, and = output(duration, first, and, "year", years)
    end
    return duration
end

function output(duration, first, and, unit, value)
    if value > 0
        unit = unit * (value > 1 ? "s" : "")
        if first
            duration = "$value $unit"
            first = false
        elseif and
            duration = "$value $unit and " * duration
            and = false
        else
            duration = "$value $unit, " * duration
        end
    end
    return duration, first, and
end