
# output should be in the format: HH:MM:SS
function humanreadable(seconds)
    hours = floor(Int, seconds / 3600)
    minutes = floor(Int, (seconds - hours * 3600) / 60)
    seconds = seconds - hours * 3600 - minutes * 60
    return join(string.((hours, minutes, seconds), pad=2), ":")
end