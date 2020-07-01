def format_duration(seconds):
    if seconds == 0: return "now"
    units = ( (31536000, "year"  ), 
              (   86400, "day"   ),
              (    3600, "hour"  ),
              (      60, "minute"),
              (       1, "second") )
    ts, t = [], seconds
    for unit in units:
        u, t = divmod(t, unit[0])
        ts += ["{} {}{}".format(u, unit[1], "s" if u>1 else "")] if u != 0 else []
    return ", ".join([str(d)for d in ts[:-1]]) + (" and " if len(ts)>1 else "") + ts[-1]
    
    
    
    
  or
  
  
  def format_duration(seconds):

    if seconds is 0: return 'now'
    
    scale = [
        ('second',          1),
        ('minute',         60),
        ('hour',        60*60),
        ('day',      60*60*24),
        ('year', 60*60*24*365) ]
       
    times = []
    for n, s in reversed(scale):
        t = seconds/s
        if t: times.append((t,n+'s' if t > 1 else n))
        seconds = seconds%s
        
    if len(times) > 1:
        return ', '.join('%d %s' % t for t in times[:-1]) + ' and %d %s' % times[-1]
    else:
        return '%d %s' % times[0]
