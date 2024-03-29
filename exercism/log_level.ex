# Log code 	Log label 	Supported in legacy apps?
# 0 	      trace 	    no
# 1 	      debug 	    yes
# 2 	      info 	      yes
# 3 	      warning 	  yes
# 4 	      error 	    yes
# 5 	      fatal 	    no
# ? 	      unknown 	  -

defmodule LogLevel do
  def to_label(level, legacy?) do
    cond do
      level == 0 && !legacy? -> :trace
      level == 1 -> :debug
      level == 2 -> :info
      level == 3 -> :warning
      level == 4 -> :error
      level == 5 && !legacy? -> :fatal
      true -> :unknown
    end
  end

  def alert_recipient(level, legacy?) do
    label = to_label(level, legacy?)

    cond do
      label in [:error, :fatal] -> :ops
      label == :unknown && legacy? -> :dev1
      label == :unknown -> :dev2
      true -> false
    end
  end
end
